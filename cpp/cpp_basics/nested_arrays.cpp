#include <iostream>

using namespace std;

int main() {
    // basic nested array
    int numberGrid[3][2] = {
        {1, 2},
        {3, 4},
        {5, 6},
    };

    cout << "numberGrid[0][1]: " << numberGrid[0][1] << endl;

    // more examples with pointers
    // int is 4 bytes, there are 50 ints so 50 * 4 = 200 bytes of memory
    int *array = new int[50];

    // allocating 50 integer pointers
    // not actually allocating memory for the array
    int **a2d = new int*[50];

    // with the above two examples...
    // the first example, we are talking about an integer.
    // since 'int *array' is an array of 50 integers.
    // and each element is an int pointer
    array[4] = 4;

    // however with the second example, we have pointers to an array.
    // thus, 'a2d[4]' is pointing to the memory of the array.
    a2d[4] = nullptr;


    return 0;
}
