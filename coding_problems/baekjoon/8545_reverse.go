package main

import "fmt"

func main() {
    var word string

    fmt.Scanf("%s", &word)

    for i:=len(word)-1; i>=0; i-- {
        fmt.Printf("%c", word[i])
    }
}
