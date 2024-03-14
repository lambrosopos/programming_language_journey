#include <stdio.h>

int main(int argc, char *argv[]) {
  int N;
  int M;

  scanf("%d %d", &N, &M);

  if(M < 3) {
    printf("NEWBIE!\n");
  } else if(M <= N) {
    printf("OLDBIE!\n");
  } else {
    printf("TLE!\n");
  }

  return 0;
}
