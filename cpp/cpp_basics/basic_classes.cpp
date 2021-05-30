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
    // Constructor when no args are given
    Book() {
      title = "No title";
      author = "No author";
      pages = 0;
    }
    // Constructor functions
    Book(string aTitle, string aAuthor, int aPages) {
      // defining values in the constructor
      title = aTitle;
      author = aAuthor;
      pages = aPages;

      cout << "Creating Object: " << title << endl;
    }

    // methods for class
    bool isOver100Pages() {
      if (pages > 100) {
        return true;
      }
      return false;
    }
};


int main() {
  // creating an object which is an instance of the class
  Book book1("Alice in Wonderland", "Lewis Carroll", 500);
  //book1.title = "Alice in Wonderland";
  //book1.author = "Lewis Carroll";
  //book1.pages = 100;
  Book book2("Spongebob", "Patrick", 50);

  cout << book1.pages << endl;
  cout << book1.title << endl;
  cout << book1.author << endl;

  cout << book1.isOver100Pages() << endl;

  cout << book2.pages << endl;
  cout << book2.title << endl;
  cout << book2.author << endl;

  cout << book2.isOver100Pages() << endl;
  return 0;
}
