#include <iostream>
using std::string;

/* OOP
 * Able to represent real-life objects,
 * explain such objects to a computer
 */

/* Access Modifiers
 * 3 in c++: Private, Public, Protected
 * Private: only accessible through class code
 * Public: can be accessed from outside
 * Protected: mixed
 */

class Employee {
public:
  // everything in class in c++ is private by default
  string Name;
  string Company;
  int Age;
};

int main()
{
  Employee employee1;
  employee1.Name = "Nyang++";
  employee1.Company = "Bulb Cat";
  employee1.Age = 10;

  return 0;
}
