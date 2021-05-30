#include <iostream>

using namespace std;

int main()
{
  bool isMale = true;
  bool isTall = true;

  // and operator
  if (isMale && isTall) {
    cout << "You are tall and male" << endl;
  } else {
    // they bail out on the first falsy condition
    cout << "You are not male" << endl;
  }

  // or operator
  if (isMale || isTall) {
    cout << "You are tall or male" << endl;
  }

  isMale = false;
  isTall = false;

  // else if and negation operator (!)
  if (!isMale && isTall) {
    cout << "You are a tall and not male" << endl;
  } else if (!isMale && !isTall) {
    cout << "You are not a male not tall" << endl;
  } else {
    cout << "You are not male" << endl;
  }

}
