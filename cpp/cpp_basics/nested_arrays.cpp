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
    // all that has been done is allocating 200 bytes of memory
    int **a2d = new int*[50];

    // with the above two examples...
    // the first example, we are talking about an integer.
    // since 'int *array' is an array of 50 integers.
    // and each element is an int pointer
    array[4] = 4;

    // however with the second example, we have pointers to an array.
    // thus, 'a2d[4]' is pointing to the memory of the array.
    // this is an integer pointer
    a2d[4] = nullptr;

    // in the end all that array does is make room for 200 byes of memory
    // now all you have to do is set each of the pointers to point to an array
    // thus ending up with 50 arrays
    
    for (int i=0; i < 50; i++)
        a2d[i] = new int[50];

    // the above for loop goes through the integer pointers
    // and changes the pointer to point to an array of 50 integers
    // basically this is a nested for loop

    // if you need more dimensions, you can simply increase the pointer
    // dimensions

    int ***a3d = new int **[50];
    for (int i = 0; i < 50; i++)
    {
        a3d[i] = new int *[50];
        for (int j = 0; j < 50; j++)
        {
            a3d[i][j] = new int[50];
            // or alternatively
            // int **ptr = a3d[i];
            // ptr[j] = new int[50];
        }
    }

    // accessing a3d
    a3d[0][0][0] = 0;

    return 0;
}
