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
    case Cons(x, xs) => x + sum(xs)
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

## 3.2 Pattern Matching

Looking deeper into functions `sum` and `product`.

Sum function
- Sum of an empty list => 0
- Sum of a nonempty list => first element + sum of remaining elements

Product function
- Product of an empty list => 1.0
- Product of any list starting with 0.0 => 0.0
- Product of any other nonempty list => first element multiplied by product of remaining elements

A pattern matches the target if there exists an assignment of variables in the pattern to subexpressions of the target that make it structurally equivalent to the target.

### Companion Objects

Companion object is an object with the same name as the data type where various conveninence functions for creating or working with values of the data type are stored.

For example, a function

```scala
def fill[A](n: Int, a: A): List[A]
```

that created a `List` with `n` copies of the element `a` the `List` companion object will be the right place to put them.

In scala, companion objects are more of a convention. The naming could have been different and be named `Foo` but calling it `List` makes it clear that the module contains functions relevant to working with lists.

### Exercise 3.1

Result of the following match expression?

```scala
val x = List(1, 2, 3, 4, 5) match {
  case Cons(x, Cons(2, Cons(4, _))) => x
  case Nil => 42
  case Cons(x, Cons(y, Cons(3, Cons(4, _)))) => x + y
  case _ => 101
}
```

Answer:
- First case of `Cons(x, Cons(2, Cons(4, _))) => x` doesn't match because of `3` isn't part of the structure.
- case `Nil` doesn't match since given target is not `Nil`
- 3rd case will match since `_` will include a structure of `Cons(5, Nil)`. So the answer will be 1 + 2 => 3
- Since 3rd case matches, it won't progress to 4th case. Otherwise it would have resulted in 101.

### Variadic functions

Function `apply` in the `object List` is a variadic function, meaning it accepts zero or more arguments of type `A`.

```scala
def apply[A](as: A*): List[A] =
  if (as.isEmpty) Nil
  else Cons(as.head, apply(astail: _*))
```

The special `_*` notation allows to pass a `Seq` to a variadic method

## 3.3 Data Sharing in functional data structures

Question: How to write functions that add or remove elements from a list?
Answer: Return a new list

When adding an element 1 to the front of an existing list, say `xs`, a new list is returned. Here, there it becomes `Cons(1, xs)`. Since lists are immutable, the `xs` isn't actually copied, only reused. This is called data sharing.

Same goes for the removal of an item in a list. We don't really need to copy the list since the list is immutable. Simply referring to the tail of the list, exclusing the head allows the ability to create a list without inefficient copying.

### Exercise 3.2

Implement the function `tail` for removing the first element of a `List`

```scala
def tail[A](l: List[A]): List[A] = l match 
  case Nil => sys.error("tail of empty list")
  case Cons(_, t) => t
```

### Exercise 3.3

Implement function `setHead` for replacing first element of a `List` with a different value

```scala
def setHead[A](l: List[A], h: A): List[A] = l match
  case Nil => sys.error("can't set head of an empty list")
  case Cons(_, ab) => Cons(h, ab)
```

### Exercise 3.4

Generalize `tail` to the function `drop`, which removes first `n` elements from a list. Takes time only proportional to the number of elements being dropped. Don't copy the entire `List`.

```scala
def drop[A](l: List[A], n: Int): List[A] = {
  if n <= 0 then l
  else l match
    case Nil => Nil
    case Cons(_, t) => drop(t, n - 1)
}
```

### Exercise 3.5

Implement `dropWhile` remove elements from the `List` prefix as long as they match a predicate.

```scala
def dropWhile[A](l: List[A], f: A => Boolean): List[A] =
  l match
    case Cons(h, t) if f(h) => dropWhile(t, f)
    case _ => l
```

To illustrate the pattern guard, the condition implements an if statement after the case statment which can use any of the variables declared in the case.