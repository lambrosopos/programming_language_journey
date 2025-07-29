package main

import (
	"log"
	"os"
	"testing"
)

func removeFile(filename string) {
  err := os.Remove(filename)
  if err != nil {
    log.Println("Unable to remove file: ", filename, ". Error: ", err)
  }
}

// func BenchmarkSingle(b *testing.B) {
//   removeFile(FILENAME)

  // b.ResetTimer()
//   WriteGoThreadsWithPool(FILENAME, 100_000_00)
// }

func BenchmarkParallel(b *testing.B) {
  removeFile(FILENAME)

  // b.ResetTimer()
  WriteGoThreadsOptimized(FILENAME, 100_000_00)
}
