#include <iostream>
using namespace std;

int main() {
  int secretNum = 7;
  int guess;
  int guessCount = 3;

  while (guessCount > 0 && secretNum != guess) {
    cout << "Enter guess (0-10): ";
    cin >> guess;
    guessCount--;
    cout << "You have " << guessCount << " guesses left" << endl;
  }

  if (guessCount) {
    cout << "Great job";
  } else {
    cout << "You lose";
  }

  return 0;
}
