#include <iostream>

using namespace std;

int main() {
  int age = 19;
  double gpa = 2.7;
  string name = "Spongebob";

  // creating a pointer variable
  // pointer variables are variables that store the memory address
  int *pAge = &age;

  // printing out the memory address of the variable
  cout << pAge << endl;

  // printing out the actual value of the memory address
  cout << *pAge << endl;

  return 0;
}
