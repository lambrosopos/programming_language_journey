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

  void IntroduceYourself() {
    std::cout << "Name - " << Name << std::endl;
    std::cout << "Company - " << Company << std::endl;
    std::cout << "Age - " << Age << std::endl;
  }
  /* Constructors
   *
   * Constructors are special methods that are invoked
   * when initiating an object
   * 
   * When a constructor is not given, c++ uses a default constructor
   *
   * Creating a constructor has 3 rules:
   *
   * 1) Does not have a return value
   * 2) Has the same name as the class
   * 3) Constructor has to be public (not always)
   */
  Employee(string name, string company, int age) {
    Name = name;
    Company = company;
    Age = age;
  }
};

int main() {
  Employee employee1 = Employee("Patrick", "Bikini Ltd.", 14);
  employee1.IntroduceYourself();

  Employee employee2 = Employee("John", "Amazon", 35);
  employee2.IntroduceYourself();
}
