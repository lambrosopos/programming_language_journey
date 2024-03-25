#include <stdio.h>

int main(int argc, char *argv[]) {
  int A, B, C;

  scanf("%d %d", &A, &B);
  scanf("%d", &C);

  if(A + B >= C * 2) {
    printf("%d", A + B - (C * 2));
  } else {
    printf("%d", A + B);
  }

  return 0;
}
