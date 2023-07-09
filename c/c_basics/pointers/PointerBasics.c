/* Pointer Basics
* "Pointers store memory addresses."
* Since pointers store memory addresses, it needs to know
* what type of value it is pointing at.
* The reason the type of pointer also needs to be declared is because
* when the derefencing happens, it needs to know how to read the data.
* For example, if it's an int type, it will only read 4 bytes.
*/

#include <stdio.h>

int main(void) {
    int num = 7;
    int * int_ptr = &num;
    printf("The address: %p contains %d \n", int_ptr, num);

    return 0;
}