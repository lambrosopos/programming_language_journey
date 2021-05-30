#include <iostream>

using namespace std;

int getMax(int num1, int num2) {
  int result;

  if (num1 > num2) {
    result = num1;
  } else {
    result = num2;
  }

  return result;
}

int main() {
  int result = getMax(2, 4);

  cout << "higher num is : " << result << endl;

  return 0;
}
