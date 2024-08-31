package main

import (
  "fmt"
  "sync"
  "time"
)


var mutux sync.Mutex


type Account struct {
  Balance int
}

/*
Adding and Subtracting from a variable that has been changed leads to wrong value output

for e.g.
  1. A, B routine reads 1000 account balance.
  2. A adds 1000 and B also adds 1000 to 1000
  3. A => balance = 1000 + 1000 (original balance), B => balance = 1000 + 1000 (original balance)
  4. both return 2000

this is the same for subtraction
*/
func DepositAndWithDraw(account *Account) {
  mutux.Lock()
  defer mutux.Unlock()

  if account.Balance < 0 {
    panic(fmt.Sprintf("Balance should not be negative value : %d", account.Balance))
  } else if account.Balance > 10000 {
    panic(fmt.Sprintf("Balance should not go over 10000 : %d", account.Balance))
  }

  account.Balance += 1000 
  fmt.Printf("Current balance: %d\n", account.Balance)
  time.Sleep(time.Nanosecond)
  account.Balance -= 1000
  fmt.Printf("Current balance: %d\n", account.Balance)
}

func main() {
  var wg sync.WaitGroup

  wg.Add(10)

  account := &Account{0}

  for i:=0; i<10; i++ {
    go func() {
      for {
        DepositAndWithDraw(account)
      }
      wg.Done()
    }()
  }

  wg.Wait()
}
