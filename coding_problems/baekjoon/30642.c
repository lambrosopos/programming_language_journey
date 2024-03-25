#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  int N;
  char M[8];
  int F;

  scanf("%d", &N);
  scanf("%s", M);
  scanf("%d", &F);

  if(strcmp(M, "induck")) {
    if(F % 2 == 0) {
      printf("%d\n", F - 1);
    } else {
      printf("%d\n", F);
    }
  } else {
    if(F % 2 == 0) {
      printf("%d\n", F);
    } else {
      if(F == N) {
        printf("%d\n", F - 1);
      } else {
        printf("%d\n", F + 1);
      }
    }
  }

  return 0;
}
