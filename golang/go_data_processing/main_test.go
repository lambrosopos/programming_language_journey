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

func SingleWriter1_000_000(b *testing.B) {
  removeFile(FILENAME)

  b.ResetTimer()
  WriteSingleProcessor(FILENAME, 1_000_000)
}

func SingleWriter10_000_000(b *testing.B) {
  removeFile(FILENAME)

  b.ResetTimer()
  WriteSingleProcessor(FILENAME, 10_000_000)
}

func GoRoutineWriter10_000_000(b *testing.B) {
  removeFile(FILENAME)

  b.ResetTimer()
  WriteGoThreads(FILENAME, 10_000_000)
}
