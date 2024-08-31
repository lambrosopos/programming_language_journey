package main

import (
  "fmt"
  "time"
  "sync"
)

func square_3(wg *sync.WaitGroup, ch chan int) {
  tick := time.Tick(time.Second)
  terminate := time.After(10 * time.Second)

  for {
    select {
      case <- tick:
        fmt.Println("Tick")
      case <- terminate:
        fmt.Println("Terminated")
        wg.Done()
        return
      case n:= <- ch:
        fmt.Printf("Square: %d\n", n*n)
        time.Sleep(time.Second)
    }
  }
}

func main() {
  var wg sync.WaitGroup
  var ch chan int = make(chan int)

  wg.Add(1)
  go square_3(&wg, ch)
  
  for i:=0; i<5; i++ {
    ch <- i * 2
  }

  wg.Wait()
}
