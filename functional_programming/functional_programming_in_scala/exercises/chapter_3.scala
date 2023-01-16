import java.io.File
import java.io.PrintWriter


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

object Main {
    val myFile = new File("/home/lambrosopos/coding/programming_language_journey/functional_programming/functional_programming_in_scala/exercises/test_scala.md")
    val myPrintWriter = new PrintWriter(myFile)

    myPrintWriter.write("Writing with java io in scala")
    myPrintWriter.close()
    println("Hello world!")
}