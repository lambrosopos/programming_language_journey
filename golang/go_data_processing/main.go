package main

var FILENAME string = "massive.txt"

func main() {
  // WriteSingleProcessor(FILENAME)
  WriteGoThreads(FILENAME, 10_000_000)
}
