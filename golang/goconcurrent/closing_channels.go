package main

import (
  "math/rand"
  "fmt"
  "time"
  "sync"
)


func square_2(wg *sync.WaitGroup, ch chan int) {
  for n := range ch {
    time.Sleep(time.Second)
    fmt.Printf("Square : %d\n", n*n)
  }
  wg.Done()
}


func main() {
  var wg sync.WaitGroup

  var ch chan int = make(chan int)

  wg.Add(1)
  go square_2(&wg, ch)

  for i:=0; i<5; i++ {
    ch <- rand.Intn(100)
    time.Sleep(time.Duration(rand.Intn(3)) * time.Second)
  }

  close(ch)

  wg.Wait()
}

