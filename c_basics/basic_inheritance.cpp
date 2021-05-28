#include <iostream>
using namespace std;

/* Inheritance
 * 
 * Inheritance allows other classes to mimic same methods and properties
 * same in C++
 */

class Chef {
  public:
    void makeChicken() {
      cout << "The chef makes chicken" << endl;
    }
    void makeSalad() {
      cout << "The chef makes salad" << endl;
    }
    void makeSpecialDish() {
      cout << "The chef makes bbq ribs" << endl;
    }
};

class ItalianChef : public Chef {
};

int main()
{
  Chef chef;
  chef.makeChicken();

  ItalianChef italianChef;
  italianChef.makeChicken();
  return 0;
}

