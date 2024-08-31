package main

import (
  "math/rand"
  "fmt"
  "time"
  "sync"
)


func main() {
  var wg sync.WaitGroup

  var ch chan int = make(chan int)

  var jobs int = 2

  wg.Add(jobs)

  for i:=0; i<jobs; i++ {
    go square(&wg, ch)
  }

  for i:=0; i<jobs; i++ {
    ch <- rand.Intn(100)
    time.Sleep(time.Duration(rand.Intn(3)) * time.Second)
  }

  wg.Wait()
}

func square(wg *sync.WaitGroup, ch chan int) {
  n := <- ch

  time.Sleep(time.Second)
  fmt.Printf("Square : %d\n", n*n)
  wg.Done()
}
