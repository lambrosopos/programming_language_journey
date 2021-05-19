#include <stdio.h>

int main(void) {
    // ++
    int a = 10;
    printf("a is '%d'\n", a);
    a++;
    printf("a is '%d' after ++\n", a);
    
    int b = 20;
    printf("current b: '%d'\n", b);
    printf("++b '%d'\n", ++b);
    printf("b++ '%d'\n", b++);
    printf("b '%d'\n", b);

    // for loop
    for (int i = 1; i <= 10; i++) {
        printf("i in for loop: '%d'\n", i);
    }

    // while loop
    int i = 1;
    while (i <= 10) {
        printf("i in while loop: '%d'\n", i++);
        // or you can add another line with i++
    }

    // do while
    int j = 1;
    do {
        printf("do while loop j: '%d'\n", j++);
    } while (j <= 10);

    return 0;
}
