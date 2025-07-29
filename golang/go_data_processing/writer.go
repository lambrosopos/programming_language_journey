package main

import (
	"bufio"
	"context"
	"fmt"
	"log"
	"os"
	"runtime"
	"sync"
)

// OPTIMIZED VERSION 1: Fixed issues and improved performance
func WriteGoThreadsOptimized(filename string, optionalArgs ...int) error {
	totalRows := 10_000
	if len(optionalArgs) > 0 {
		totalRows = optionalArgs[0]
	}

	file, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return fmt.Errorf("unable to open %s: %w", filename, err)
	}
	defer file.Close()

	// Larger buffer for better I/O performance
	writer := bufio.NewWriterSize(file, 64*1024) // 64KB buffer
	defer func() {
		if flushErr := writer.Flush(); flushErr != nil {
			log.Printf("Error flushing writer: %v", flushErr)
		}
	}()

	// Better worker calculation - cap at reasonable limit
	numWorkers := min(runtime.NumCPU()*2, 16, totalRows)
	if totalRows < 1000 {
		numWorkers = 1 // Don't use concurrency for small jobs
	}

	var wg sync.WaitGroup
	// Reduced channel buffer size to prevent excessive memory usage
	lineChan := make(chan []byte, numWorkers*5)
	
	// Context for graceful shutdown
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Single writer goroutine with error handling
	writerErr := make(chan error, 1)
	wg.Add(1)
	go func() {
		defer wg.Done()
		var linesWritten int64
		
		for {
			select {
			case line, ok := <-lineChan:
				if !ok {
					fmt.Printf("Writer finished. Lines written: %d\n", linesWritten)
					return
				}
				
				if _, err := writer.Write(line); err != nil {
					writerErr <- fmt.Errorf("write error at line %d: %w", linesWritten, err)
					return
				}
				linesWritten++
				
			case <-ctx.Done():
				return
			}
		}
	}()

	// Work distribution - pre-calculate work per worker
	workPerWorker := totalRows / numWorkers
	remainder := totalRows % numWorkers

	var generatorWg sync.WaitGroup
	
	for i := 0; i < numWorkers; i++ {
		generatorWg.Add(1)
		
		// Calculate work range for this worker
		start := i * workPerWorker
		end := start + workPerWorker
		if i == numWorkers-1 {
			end += remainder // Last worker handles remainder
		}
		
		go func(workerID, startIdx, endIdx int) {
			defer generatorWg.Done()
			
			// Pre-allocate buffer to reduce allocations
			buffer := make([]byte, 0, 256)
			
			for j := startIdx; j < endIdx; j++ {
				select {
				case <-ctx.Done():
					return
				default:
				}
				
				phrase := PhraseGenerator()
				
				// Reuse buffer to minimize allocations
				buffer = buffer[:0]
				buffer = append(buffer, phrase...)
				buffer = append(buffer, '\n')
				
				// Create a copy for the channel (buffer will be reused)
				line := make([]byte, len(buffer))
				copy(line, buffer)
				
				select {
				case lineChan <- line:
				case <-ctx.Done():
					return
				}
			}
		}(i, start, end)
	}

	// Wait for generators and close channel
	go func() {
		generatorWg.Wait()
		close(lineChan)
	}()

	// Wait for writer and check for errors
	wg.Wait()
	
	// Check for writer errors
	select {
	case err := <-writerErr:
		return err
	default:
	}

	fmt.Printf("Finished writing %d lines to %s using %d workers\n", totalRows, filename, numWorkers)
	return nil
}

