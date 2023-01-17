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