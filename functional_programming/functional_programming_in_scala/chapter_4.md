# Chapter 4: Handling errors without exceptions

## 4.1 The good and bad aspects of exceptions

Why do exceptions break referential transparency?

Let's look at an example:

```scala
def faillinFn(i: Int): Int = {
    val y: Int = throw new Exception("fail!")
    try {
        val x = 42 + 5
        x + y
    }
    catch { case e: Exception => 43 }
}
```

However, with referential transparency, we have to be able to substitute the reference `y` with `throw new Exception("fail")`.

Here, if substituted, it will look like this:

```scala
def faillinFn(i: Int): Int = {
    try {
        val x = 42 + 5
        x + ((throw new Exception("fail!")): Int)
    }
    catch { case e: Exception => 43 }
}
```

But the above code will result in `43` since the exception will be caught and handled.

Thus, another way of understanding RT expressions is that they don't depend on context. While non-RT expressions are context-dependent.

There are 2 main problems with exceptions:

1. exceptions break RT and introduce context dependency. Exceptions should be used for error handling not control flow.

2. Exceptions are not type-safe. The type of `failingFn, Int => Int` tells us nothing about the fact that exceptions may occur, and the compiler will certainly not force callers of `failinFn` to make a decision about how to handle these exceptions. They won't be detected until runtime.

The error handling introduced will use an old idea from C which returns new generic types for these 'possibly defined values'. Unlike C-style error codes, they will be completely type-safe and will also benefit the assistance from type detections.

## 4.2 Possible alternatives to exceptions

In the code below

```scala
def mean(xs: Seq[Double]): Double = 
  if (xs.isEmpty)
    throw new ArithmeticException("mean of empty List!")
  else xs.sum / xs.length
```

The function `mean` is an example of a partial function. 

The first possibilty is to return some sort of bogus value of type `Double`
- Return `xs.sum / xs.length` in all cases, result in `0.0 / 0.0` when empty
- Return some other sentinel value

However this solution is rejected for a few reasons:
 - Allows errors to silently propagate
 - Result in more boilerplates and `if` statements to check whether the caller has received a "real" result.
 - Not applicable to polymorphic code
 - Demands a special policy or calling convention of callers. Special policies to call such functions will lead to difficult implementation with higher order functions.

 The second possibility is to force the caller to supply an argument that tells us what to do in case we don't know how to handle the input:

 ```scala
 def mean_1(xs: IndexedSeq[Double], onEmpty: Double): Double =
  if (xs.isEmpty) onEmpty
  else xs.sum / xs.length
```

This makes `mean` to be a total function (different from a partial function from the first example). 

However this also has some drawbacks.
 - Requires that immediate callers have direct knowledge of how to handle the undefined case
 - Limits to returning a `Double`
 - What if `mean_1` was part of a larger computation and needs to be exited when undefined?

## 4.3 The option data type

Solution is to represent explicitly in the return type that a function may not always have an answer.

This strategy is deferring to the caller for the error-handling. Introduce a new type `Option`. 

The type `Option` exists in the scala library.

```scala
sealed trait Option[+A]
case class Some[+A](get: A) extends Option[A]
case object None extends Option[Nothing]
```

The above code can be used to define the function `mean`

```scala
def mean(xs: Seq[Double]): Option[Double] =
  if (xs.isEmpty) None
  else Some(xs.sum / xs.length)
```

Since we still return a type `Option[Double]` even when the list is empty, `mean` is now a total function. 

## 4.4 The Either data type

The concept of handling errors in functional programming is to handle them using ordinary values, also using common patterns of error handling and recovery.

`Option` is not the only option we can use. And while it is available, it is quite simplistic. One characteristic about using `Option` is that it doesn't tell you about the actual error, only returning a `None` value.

Sometimes when just knowing that a failure occurred is sufficient, an `Option` data type is enough. However, when figuring out the reason for the failure, we can use an `Either` data type.

### Either data type definition

`Either` has only two cases, just like `Option`. Unlike `Option`, both cases for `Either` data type carries a value. The values can be said to be a disjoint union of two types.

The two cases can be expressed as `Left` or `Right` cases, where the right value is expressed using `Right` as a pun.

Both `Option` and `Either` data types are included in the Scala standard library since they are used quite commonly.

Let's look into the `mean` example again, this time with `Either` data type.

```scala
def mean(xs: IndexedSeq[Double]): Either[String, Double] =
  if (xs.isEmpty)
    Left("Mean of empty List")
  else
    Right(xs.sum / xs.length)
```

The above example shows the basic usage of `Either` data type. `Either[String, Double]` represents the type to be returned. When available, the `Double` data type is returned while with an error, `String` data type is returned.

Let's look into another example.

Sometimes, when more information is needed, for example, a stack trace, we can also return the Exception itself in the `Left` side of `Either`.

```scala
def safeDiv(x: Int, y: Int): Either[Exception, Int] = 
  try Right(x / y)
  catch { case e: Exception => Left(e) }
```

Since the `try... catch` pattern is very common, we can create a `Try` function to handle such patterns.

```scala
def Try[A](a: => A): Either[Exception, A] =
  try Right(a)
  catch { case e: Exception => Left(e) }
```

And by using the above two examples, we can now write out the function as such.

```scala
def parseInsuranceRateQuote(
  age: String,
  numberOfSpeedingTickets: String): Either[Exception, Double] = 
    for {
      a <- Try { age.toInt }
      tickets <- Try { numberOfSpeedingTickets.toInt }
    } yield insuranceRateQuote(a, tickets)
```

## Summary

The biggest idea in FP in handling errors is to represent them using ordinary values and use higher-order functions to hande common patterns.