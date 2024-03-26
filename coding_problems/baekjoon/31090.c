#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  int T;
  char Y[4];

  scanf("%d", &T);

  int i;
  for(i=0; i<T; i++) {
    scanf("%s", Y);

    if((atoi(Y) + 1) % atoi(&Y[2]) == 0) {
      printf("Good\n");
    } else {
      printf("Bye\n");
    }
  }

  return 0;
}
