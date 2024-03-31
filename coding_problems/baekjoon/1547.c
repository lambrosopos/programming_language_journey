#include <stdio.h>

int main(int argc, char *argv[]) {
  int T;
  int A, B, temp;
  int C[4]={0, 1, 0, 0};

  scanf("%d", &T);

  int i;
  for(i=0; i<T; i++) {
    scanf("%d %d", &A, &B);

    temp=C[A];
    C[A]=C[B];
    C[B]=temp;
  }

  for(i=0; i<4; i++) {
    if(C[i] == 1) {
      printf("%d\n", i);
    }
  }

  return 0;
}
