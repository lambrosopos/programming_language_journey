#include <iostream>

using namespace std;

/* Classes
 * classes are basically a new data type
 * we can make custom types to represent data
 */

// class names are capitals
class Book {
  // mapping out a blueprint for a book datatype
  public:
    string title;
    string author;
    int pages;
};


int main() {
  // creating an object which is an instance of the class
  Book book1;
  book1.title = "Alice in Wonderland";
  book1.author = "Lewis Carroll";
  book1.pages = 100;

  cout << book1.pages << endl;
  cout << book1.title << endl;
  cout << book1.author << endl;

  return 0;
}
