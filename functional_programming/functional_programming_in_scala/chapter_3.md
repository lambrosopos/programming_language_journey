# Chapter 3: Functional data structures

## 3.1 Defining functional data structures

A functional data structure is operated on using only pure functions. Therefore, functional data structures are by definition immutable.

Example using linked list.

```scala
package fpinscala.datastructures

sealed trait List[+A]
case object Nil extends List[Nothing]
case class Cons[+A](head: A, tail: List[A]) extends List[A]

object List {
  def sum(ints: List[Int]): Int = ints match {
    case Nil => 0
    case Cons(x, xs)) => x + sum(xs)
  }

  def product(ds: List[Double]): Double = ds match {
    case Nil => 1.0
    case Cons(0.0, _) => 0.0
    case Cons(x, xs) => x * product(xs)
  }

  def apply[A](as: A*): List[A] =
    if (as.isEmpty) Nil
    else Cons(as.head, apply(as.tail: _*))
}
```

Code explanation:
 - trait: trait introduces a data type. An abstract interface that may optionally contain implementations of some methods.
 - sealed trait: the keyword sealed in sealed trait means that all implementations of the trait must be declared in this file.
 - `+` means that the type parameter can be covariant

More about variance (+)

In `trait List[+A]`, the `+` is a variance annotation that signals that `A` is a covariant or positive parameter of List.

Companion Objects
A companion object is just an object with the same name as the data type where we put various convenience functions for creating or working with values of the data type.