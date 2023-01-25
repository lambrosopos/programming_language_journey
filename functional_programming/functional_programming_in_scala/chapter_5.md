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

## 5.1 Strict and non-strictness

What is strictness?

Strictness in a function can be defined as evaluating the arguments passed to a function right away. Depending on the language, strictness is sometimes enforced. For scala, unless told otherwise, any function defined will be strict.

For example,

Receiving a code such as `square(41.0 + 1.0)` the function will evaluate `41.0 + 1.0` before the function operates. Same goes for `square(sys.error('failure'))`, scala will raise a system error with a 'failure' message before the function even has a chance to operate. This is because it is strict. It will evalute its arguments right away.

Some examples of strictness is the `&&` and `||` operators. Using these operators, one can use a short circuit concept to not evaluate the latter value.

Another example is the `if` statement which also doesn't evaluate depending on the condition. To be clear, the `if` statement is strict in terms of evaluating the conditions.

Let's look at the non-strict function syntax

```scala
def if2[A](cond: Boolean, onTrue: () => A, onFalse: () => A): A =
    if (cond) onTrue() else onFalse()
```

The above example is a basic example of creating a non-strict function in scala. In the upcoming examples, there will be a better example that sugarcoats this concept.


