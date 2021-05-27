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
      setRating(aRating);
    }

    void setRating(string aRating) {
      if (aRating == "G" || aRating == "PG" || aRating == "R" || aRating == "PG-13") {
        rating = aRating;
      };
    }
};

int main() {
  Movie avengers("The Avengers", "joss Whedon", "PG-13");

  avengers.setRating("R");

  cout << avengers.rating << endl;
  return 0;
}

