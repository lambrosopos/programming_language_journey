#include <stdio.h>

int main(int argc, char *argv[]) {
  int A, B;

  scanf("%d %d", &A, &B);

  if(B >= A) {
    printf("%d\n", 2*A-1);
  } else {
    printf("%d\n", 2*B+1);
  }

  return 0;
}
