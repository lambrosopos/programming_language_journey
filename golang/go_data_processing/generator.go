package main

import (
	"fmt"
	"math/rand"
)

var RANDOM_WORDS_LEVEL_1 = []string{
  "cat",
  "dog",
  "innovator",
  "compass",
  "milk",
  "book",
  "monitor",
  "cola",
}

var RANDOM_WORDS_LEVEL_2 = []string{
  "delicious",
  "hateful",
  "loving",
  "positive",
  "negative",
  "medieval",
}

func PhraseGenerator() []byte {
  
  first_word := RANDOM_WORDS_LEVEL_1[rand.Intn(len(RANDOM_WORDS_LEVEL_1))]
  second_word := RANDOM_WORDS_LEVEL_2[rand.Intn(len(RANDOM_WORDS_LEVEL_2))]

  name := fmt.Sprintf("%s %s", second_word, first_word)

  return []byte(name)
}
