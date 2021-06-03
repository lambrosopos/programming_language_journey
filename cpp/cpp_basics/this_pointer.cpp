#include <iostream>
using namespace std;

/* 'this' pointer in c++
 *
 * 1. Each object gets its own copy of the data member.
 * 2. All-access the same function definition as present in the code segment
 *
 * The 'this' pointer is passed as a hidden argument to all nonstatic member function calls
 * and is available as local variable within the body of all nonstatic functions.
 * 
 * 'this' pointer is not available in static member functions as static member functions
 * can be called without any object (with class name)
 *
 * ex.) For a class X, the type of this pointer is 'X*'
 *
 * Also if a member function of X is declared as const, then the type of this pointer is
 * 'const X*'
 *
 * You can destroy an C++ object by calling 'delete this;'
 */

// Use case 1: local variable's name same as member's name
class Case1
{
    private:
        int x;
    public:
        void setX (int x)
        {
            this->x = x;
        }
        void print(int x) 
        {
            // you can reference specific member's value with this
            cout << "x = " << this->x << endl;
        }
};

// for case 1
//int main()
//{
    //Case1 obj_1;
    //int x = 20;
    //obj_1.setX(x);
    //obj_1.print(40);

    //Case1 obj_2;
    //obj_2.setX(25);
    //obj_2.print(45);
    //return 0;
//}

// Use case 2: return reference to the calling object
class Case2
{
    private:
        int x;
        int y;
    public:
        Case2(int x = 0, int y = 0)
        {
            this->x = x;
            this->y = y;
        }
        Case2 &setX(int a)
        {
            x = a;
            return *this;
        }
        Case2 &setY(int b)
        {
            y = b;
            return *this;
        }
        void print()
        {
            cout << "x = " << x << " y = " << y << endl;
        }
};

int main()
{
    Case2 obj1(5, 5);

    obj1.setX(10).setY(20);

    obj1.print();
    return 0;
}
