package main

import (
  "fmt"
  "time"
  "sync"
)


type Car struct {
  Body string
  Tire string
  Color string
}

var wg sync.WaitGroup
var startTime = time.Now()
var carIdx int = 0

func main() {
  var tireCh chan *Car = make(chan *Car)
  var colorCh chan *Car = make(chan *Car)

  fmt.Printf("Start factory...\n")

  wg.Add(3)
  go MakeBody(tireCh)
  go MakeTire(tireCh, colorCh)
  go MakeColor(colorCh)

  wg.Wait()

  fmt.Printf("Finished factory...")
}

func MakeBody(tireCh chan *Car) {
  tick := time.Tick(time.Second)
  terminate := time.After(time.Second * 10)

  for {
    select {
    case <- tick:
      car := &Car{}
      car.Body = "Sports Car"
      tireCh <- car
      // fmt.Printf("Starting car %d...\n", carIdx)
      carIdx++
    case <- terminate:
      close(tireCh)
      wg.Done()
      return
    }
  }
}

func MakeTire(tireCh chan *Car, colorCh chan *Car) {
  for car := range tireCh {
    time.Sleep(time.Second)
    car.Tire = "Snow Tire"
    colorCh <- car
  }
  wg.Done()
  close(colorCh)
}

func MakeColor(colorCh chan *Car) {
  for car := range colorCh {
    time.Sleep(time.Second)
    car.Color = "SkyBlue"
    
    duration := time.Now().Sub(startTime)
    fmt.Printf("%.2f Complete Car: %s %s %s\n", duration.Seconds(), car.Body, car.Tire, car.Color)
  }
  wg.Done()
}
