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
    printf("The address: %p has a size of: %lu and contains %d \n", int_ptr, sizeof(int_ptr), *int_ptr);

    // Declaring multiple variables of same type
    int num2, * num2_ptr;

    *int_ptr += 20;
    printf("Adding 20 to memory referenced by pointer results in: %d \n", *int_ptr);

    // It can be dangerous to assign values without assignment
    int * num3_ptr; // No value assigned -> filled with garbage value
    *num3_ptr = 100; // Dangerous to perform since we don't know where this pointer pointing at

    printf("Current dangerous pointer memory: %p with value: %d \n", num3_ptr, *num3_ptr);

    // Another dangrous use of pointer initializations
    int * num4_ptr = 125; // The compiler recognizes 125 as an 'int' which is not compatible with type 'int *'
    *num4_ptr = 10;

    printf("Current dangerous pointer memory: %p with value: %d \n", num4_ptr, *num4_ptr);

    return 0;
}