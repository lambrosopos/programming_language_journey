# Chapter 1: What is functional programming?

"Functional programming is a restriction on how we write programs not on what programs can express"

2 Important concepts in FP
- referential transparency
- substitution model

## 1.1 The benefits of FP: Simple example

scala program with side effects

```scala
class Cafe {
  def buyCoffee(cc: CreditCard): Coffee = {
    val cup = new Coffee()
    cc.charge(cup.price)
    cup
  }
}
```

`cc.charge(cup.price)` is an example of side effect, an impure program. Since 'charging a credit card' is an action from the outside world, while the function itself only returns an instance of `Coffee()`, it can be seen as a side effect.

The charge action can be changed by seperating the credit card charge logic from the credit card itself. This is because the credit card shouldn't have to know the logic of charging a cost.

The code can be written as such.

```scala
class Cafe {
  def buyCoffee(cc: CreditCard, pp: Payments): Coffee = {
    val cup = new Coffee()
    pp.charge(cup.price)
    cup
  }
}
```

Although the side effect still exists with charging, the testability has been increased since we can control the payments charge logic differently from the credit card logic.

What if the customer wants to order 12 cups of coffee? Should we loop 12 times using `buyCoffee` function? That means the customer will be charged 12 times and the coffee shop will send 12 transactions to the credit card company. That means more fees and is bad for both the customer and the shop.

Here, we can seperate the side effect, sending transactions to charge, from the calculating payments part.

```scala
class Cafe {
  def buyCoffee(cc: CreditCard): (Coffee, Charge) = {
    val cup = new Coffee()
    (cup, Charge(cc, cup.price))
  }
}
```

The above code sepeartes the concern from payment and charge. The `Charge` type is actually a custom data type that can also hold a method `combine` to merge charges for the same credit card.

```scala
case class Charge(cc: CreditCard, amount: Double) {
  def combine(other: Charge): Charge =
    if (cc == other.cc)
      Charge(cc, amount + other.amount)
    else
      throw new Exception("Can't combine charges to different cards")
}
```

Now using the ability to add charges together, we can also implement a `buyCoffees` function to process multiple orders of coffee.

```scala
class Cafe {
  def buyCoffee(cc: CreditCard): (Coffee, Charge) = ...

  def buyCoffees(cc: CreditCard, n: Int): (List[Coffee], Charge) = {
    val purchases: List[(Coffee, Charge)] = List.fill(n)(buyCoffee(cc))
    val (coffees, charges) = purchases.unzip
    (coffees, charges.reduce((c1, c2) => c1.combine(c2)))
  }
}
```

Because `Charge` has been made into a first-class, we can use this concept to our advantage. For example we can add a `coalesce` function to `Charge` to group charges for each credit card.

```scala
def coalesce(charges: List[Charge]): List[Charge] =
  charges.groupBy(_.cc).values.map(_.reduce(_ combine _)).toList
```


