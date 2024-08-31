package main

import (
  "fmt"
  "math/rand"
  "sync"
  "time"
)


var wg sync.WaitGroup


func main() {
  rand.Seed(time.Now().UnixNano())

  wg.Add(2)
  fork := &sync.Mutex{}
  spoon := &sync.Mutex{}

  go diningProblem("A", fork, spoon, "fork", "spoon") // A takes fork first
  go diningProblem("B", spoon, fork, "spoon", "fork") // B takes fork first

  wg.Wait()
}

func diningProblem(name string, first *sync.Mutex, second *sync.Mutex, firstName string, secondName string) {
  for i:=0; i<100; i++ {
    fmt.Printf("%s tries to eat\n", name)
    first.Lock()
    fmt.Printf("%s obtains %s\n", name, firstName)
    second.Lock()
    fmt.Printf("%s obtains %s\n", name, secondName)

    fmt.Printf("%s eats\n", name)
    time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)

    second.Unlock()
    first.Unlock()
  }

  wg.Done()
}

