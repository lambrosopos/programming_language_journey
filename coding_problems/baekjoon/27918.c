#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  int N;
  char winner;

  int D=0;
  int P=0;

  scanf("%d", &N);

  int i;
  for(i=0; i<N; i++) {
    scanf(" %c", &winner);

    if(abs(D-P) >= 2) {
      continue;
    }

    winner == 'D' ? D++ : P++;
  }

  printf("%d:%d\n", D, P);

  return 0;
}
