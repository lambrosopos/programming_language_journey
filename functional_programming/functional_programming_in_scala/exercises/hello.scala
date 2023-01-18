def faillinFn(i: Int): Int = {
    val y: Int = throw new Exception("fail!")
    try {
        val x = 42 + 5
        x + y
    }
    catch { case e: Exception => 43 }
}

faillinFn(12)