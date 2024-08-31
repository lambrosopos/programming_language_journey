package main

import (
  "fmt"
  "sync"
  "time"
)


type Job interface {
  Do()
}

type SquareJob struct {
  index int
}

func (j *SquareJob) Do() {
  fmt.Printf("Start Job : %d\n", j.index)
  time.Sleep(time.Second * 1)
  fmt.Printf("Job %d complete - results : %d\n", j.index, j.index * j.index)
}

func main() {
  var jobList [10]Job

  for i:=0; i<10; i++ {
    jobList[i] = &SquareJob{i}
  }

  var wg sync.WaitGroup
  wg.Add(10)

  for i:=0; i<10; i++ {
    job := jobList[i]
    go func() {
      job.Do()
      wg.Done()
    }()
  }
  wg.Wait()
}
