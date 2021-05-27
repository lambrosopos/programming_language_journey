#include <iostream>

using namespace std;

class Movie {
  private:
    string rating;
  public:
    string title;
    string director;

    Movie(string aTitle, string aDirector, string aRating) {
      title = aTitle;
      director = aDirector;
      rating = aRating;
    }
};

int main() {
  Movie avengers("The Avengers", "joss Whedon", "PG-13");

  cout << avengers.rating << endl;
  return 0;
}

