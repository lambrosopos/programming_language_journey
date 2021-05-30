#include <iostream>

using namespace std;

int main() {
  int index = 1;
  while (index <= 5) {
    if (index == 3) {
      index++;
      continue;
    }

    cout << index << endl;
    index++;
  }
  return 0;
}
