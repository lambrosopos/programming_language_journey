package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"runtime"
	"sync"
	"sync/atomic"
)

func WriteSingleProcessor(filename string, optionalArgs ...int) {
  // Write synchronously to a file
  totalRows := 10_000
  if len(optionalArgs) > 0 {
    totalRows = optionalArgs[0]
  }

  file, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0777)
  if err != nil {
    log.Fatal("Unable to open file:", filename, "\nError:", err)
  }

  defer file.Close()

  for range(totalRows) {
    newPhrase := append(PhraseGenerator(), '\n')

    _, err := file.Write(newPhrase)
    if err != nil {
      log.Fatal("Unable to write to file:", string(newPhrase), "\nError:", err)
    }
  }
  
  fmt.Println("Finished writing ")
}

// Optimized WriteGoThreads function
func WriteGoThreads(filename string, optionalArgs ...int) {
	totalRows := 10_000
	if len(optionalArgs) > 0 {
		totalRows = optionalArgs[0]
	}

	file, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0666) // Changed permissions to 0666
	if err != nil {
		log.Fatalf("Unable to open %s. %s", filename, err)
	}
	defer file.Close() // Ensure the file is closed

	// Use a buffered writer for efficiency
	writer := bufio.NewWriter(file)
	defer writer.Flush() // Ensure all buffered data is written before file is closed

	// Determine the number of workers based on CPU cores or a fixed number
	numWorkers := runtime.NumCPU() * 2 // A common heuristic: 2x CPU cores
	if numWorkers > totalRows {
		numWorkers = totalRows // Don't create more workers than rows if totalRows is small
	}
	if numWorkers == 0 { // Handle case where totalRows is 0 or very small
		numWorkers = 1
	}

	var wg sync.WaitGroup
	lineChan := make(chan []byte, numWorkers*10) // Buffered channel to hold lines to be written

	// Start a single writer goroutine
	wg.Add(1)
	go func() {
		defer wg.Done()
		var linesWritten atomic.Int64 // Using atomic for a thread-safe counter
		for line := range lineChan {
			_, err := writer.Write(line)
			if err != nil {
				log.Printf("Error writing line: %v", err)
				// Depending on your error handling strategy, you might want to stop or retry
			}
			linesWritten.Add(1)
		}
		fmt.Printf("Writer goroutine finished. Total lines written by writer: %d\n", linesWritten.Load())
	}()

	// Goroutines to generate phrases and send them to the channel
	var generatorWg sync.WaitGroup
	var generatedCount atomic.Int64 // To track how many lines are generated

	// Launch multiple generator goroutines
	for i := 0; i < numWorkers; i++ {
		generatorWg.Add(1)
		go func(workerID int) {
			defer generatorWg.Done()
			for {
				currentGenerated := generatedCount.Add(1)
				if currentGenerated > int64(totalRows) {
					break // Stop if we've generated enough lines
				}
				newPhrase := append(PhraseGenerator(), '\n')
				lineChan <- newPhrase // Send the generated phrase to the writer
			}
			//fmt.Printf("Generator %d finished.\n", workerID)
		}(i)
	}

	// Wait for all generator goroutines to complete their work
	generatorWg.Wait()
	close(lineChan) // Close the channel when all generators are done, signaling the writer to exit

	// Wait for the single writer goroutine to finish processing all lines
	wg.Wait()

	fmt.Printf("Finished writing %d lines to %s using optimized Go routines.\n", totalRows, filename)
}

