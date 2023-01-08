# Chapter 2: Getting started with functional programming in Scala

## 2.1 Introducing Scala the language: an example

```scala
// A comment
/* Another Comment */
/** Documentation comment */
object MyModule {
  def abs(n: Int): Int =
    if (n < 0) -n
    else n

  private def formatAbs(x: Int) = {
    // val is an immutable variable
    val msg = "The absolute value of %d is %d"
    msg.format(x, abs(x))
  }

  // Unit is same as void in C or Java
  def main(args: Array[String]): Unit =
    println(formatAbs(-42))
}
```

`abs` function is pure since it will return the absolute value of the given integer and do nothing else. On the other hand, the `main` function is impure and sometimes called a procedure.
This is because the main function calls on a pure function as well as printing a message. It does 2 things while it's main purpose is to print a message.

The `main` method is special since Scala will look for this when running the program.

## 2.3 Modules, objects, and namespaces

`MyModule` is a namespace. Every value in Scala is an object. Each object may have 0 or more members. An object whose primary purpose is giving its members a namespace is sometimes called a module.
Member can be a method decalred with the `def` keyword, or it can be another object decalred with `val` or `object`.

Accessing the members inside the object can be done with dot notation. Namespace + . + Member -> e.g. MyModule.abs(-42). Since -42 is also an object, a `toString` member can be used on it like -42.toString

## 2.4 Higher-order functions: passing functions to functions

Writing a loop in functional format

```scala
def factorial(n: Int): Int = {
  def go(n: Int, acc: Int): Int = 
    if (n <=0) acc
    else go(n-1, n*acc)

  go(n, 1)
}
```

## 2.5 Polymorphic functions: abstracting over types

Monomorphic functions are functions that returns the same type as the input type. These functions only operate on a single type.
- Input type = Output type.
- Operates on only one type

Polymorphic functions are functions that operate on multiple types of data.

Example of polymorphic function

```scala
def findFirst(ss: Array[String], key: String): Int = {
  @annotation.tailrec
  def loop(n: Int): Int =
    if (n >= ss.length) -1
    else if (ss(n) == key) n
    else loop(n + 1)

  loop(0)
}
```

The shows how to loop by using functional programming.

Changing to a polymorphic function is as follows

```scala
def findFirst[A](as: Array[A], p: A => Boolean): Int = {
  @annotation.tailrec
  def loop(n: Int): Int =
    if (n >= as.length) -1
    else if (p(as(n))) n
    else loop(n + 1)

  loop(0)
}
```

A polymorphic function doesn't hardcode types. The above code uses a custom type `A` instead of hardcoding `String` type or other types.
Also by using a function `p` and passing in the element of type `A`, we can check if element is equal to the key value.

Exercise 2.2

Implement `isSorted, which checks whether an `Array[A]` is sorted according to a given comparison function:

```scala
def isSorted[A](as: Array[A], ordered: (A,A) => Boolean): Boolean = {
  @annotation.tailrec
  def loop(n: Int): Boolean =
    if (n >= as.length - 1) then true
    else if (ordered(as(n), as(n + 1))) then loop(n + 1)
    else false

  loop(0)
}
```

You can call HOF with anonymous functions in scala

```scala
scala> findFirst(Array(7, 9, 13), (x: Int) => x == 9)
res2: Int = 1
```

A partial function can be written as follows

```scala
def partial1[A,B,C](a: A, f: (A, B) => C): B => C =
  b: B => f(a, b)
```

The above function is like a little puzzle since at first you define each parts and assign types.
This function receives type `A` and returns a function that needs a type `B` that will in turn return a type `C`.

Exercise 2.3

Converts a function `f` of two arguments into a function of one argument that partially applies `f`.

```scala
def curry[A,B,C](f: (A, B) => C): A => (B => C) =
  a: A => partial1(a, f)
```

The function `curry` will use function `partial1` which returns a function that returns a type `C` from type `B`.

Exercise 2.4

Implement `uncurry` which reverses the transformation of `curry`. `A => (B => C)` can be written as `A => B => C`.

```scala
def uncurry[A,B,C](f: A => B => C): (A, B) => C =
  (a: A, b: B) => f(a)(b)
```

Exercise 2.5

Implement the higher-order function that composes two functions

```scala
def compose[A,B,C](f: B => C, g: A => B): A => C =
  a: A => f(g(a))
```

The above function `compose` is a common thing and can be usually expressed as `g composes f`. Composes can also be seen as an `andThen` method.

```scala
scala> val f = (x: Double) => math.Pi / 2 - x
f: Double => Double = <function1>

scala> val cos = f andThen math.sin
cos: Double => Double = <function1>
```

## 2.7 Summary

- Introduction to Scala language
- Preliminary functional programming concepts
- Define simple programs and functions
- Express loops using recursions
- Idea of higher-order functions
- Practice writing polymorphic functions in Scala
- One can follow the types of polymorphic functions and they are more constrained
