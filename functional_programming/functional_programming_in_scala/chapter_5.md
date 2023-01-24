# Chapter 5: Strictness and laziness

Before diving in, think of a situation where you have a deck of cards. For all odd numbered card, you are to take them out of the deck and for all queens, you are to flip them upside down in the deck.

You could go through the deck twice, once filtering out all odd numbered cards then another time flipping the queens.

However, you can simply go through the deck once, applying both rules at the same time.

This chapter relates to such method, of how to process through the cards and apply different methods.

Let's take a look at the following scala example.

```scala
scala> List(1, 2, 3, 4).map(_ + 10).filter(_ % == 0).map(_ * 3)
```

The above example goes through the list 3 times. However, for each operation, a temporary list is created to contain intermediary results.

A manual expression of the steps that will be taken is as follows.

1. `List(1, 2, 3, 4).map(_ + 10).filter(_ % == 0).map(_ * 3)`
2. `List(11, 12, 13, 14).filter(_ % == 0).map(_ * 3)`
3. `List(12, 14).map(_ * 3)`
4. `List(36, 42)`

Looking at this, although we can replace the intermediary List data structures for each step, wouldn't it be nicer if one can progress through the list without such results?

