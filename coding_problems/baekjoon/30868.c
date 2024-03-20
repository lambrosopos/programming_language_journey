#include <stdio.h>

int main(int argc, char *argv[]) {
  int N;
  int i, j;
  int T;

  scanf("%d", &N);

  for(i=0; i<N; i++) {
    scanf("%d", &T);

    for(j=0; j<T/5; j++) {
      printf("++++ ");
    }

    for(j=0; j<T%5; j++) {
      printf("|");
    }

    printf("\n");
  }

  return 0;
}
