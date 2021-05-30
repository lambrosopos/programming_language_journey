#include <string>
#include <iostream>

using namespace std;

int main() {
  // you have to store the same value of pointer is pointing at
  string name = "Spongebob";
  string *pName = &name;

  int age = 19;
  double gpa = 2.7;


  // creating a pointer variable
  // pointer variables are variables that store the memory address
  int *pAge = &age;

  // printing out the memory address of the variable
  cout << pAge << endl;

  // dereferencing
  // printing out the actual value of the memory address
  cout << *pAge << endl;

  // you can also just dereference a value
  // this is the same as *pAge
  cout << *&age << endl;

  return 0;
}
