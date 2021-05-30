#include <stdio.h>

int main(void) {
    /*c 에서는 세미콜론이 필수인듯*/
    // 여러 줄인 경우에는 /*...*/ 를 사용할 수 있다.
    // 한 줄로 주석처리를 하는 경우에는 // 로 처리 가능
    int age = 12;
    printf("int: %d\n", age);

    /* 실수형 예제 */
    float f = 46.5f;
    printf("float: %.2f\n", f);

    // double 도 존재한다.
    double d = 4.428;
    printf("double: %.2lf\n", d);

    /* 상수 
     * 한번 정의하면 끝임
     * 대문자로 정의
     * */
    // 앞에 const 만 입력해주면 된다.
    const int YEAR = 2000;
    printf("Year born: %d\n", YEAR);


    /* printf */
    int add = 3 + 7; // 10
    printf("3 + 7 = %d\n", add);
    printf("using printf: %d + %d = %d\n", 3, 7, 3 + 7);


    /* scanf */
    // input 을 받아 저장할 때
    int input;
    printf("Enter a value: ");
    scanf("%d", &input);
    printf("input value: %d\n", input);

    /* single char */
    char c = 'A';
    printf("char: %c\n", c);

    /* string */
    char str[256];
    printf("Enter a string under 256 characters: ");
    scanf("%s", str);
    printf("%s\n", str);


    return 0;
}
