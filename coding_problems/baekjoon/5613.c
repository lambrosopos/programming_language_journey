#include <stdio.h>

int main(int argc, char *argv[]) {
  int N;
  char C;
  int is_initialized = 0;
  int is_num = 1;

  int T;

  while(1) {
    if(is_num == 1) {
      scanf("%d", &N);

      if(is_initialized == 0) {
        T = N;
        is_initialized = 1;
      } else {
        if(C == '+') {
          T += N;
        } else if(C == '-') {
          T -= N;
        } else if(C == '*') {
          T *= N;
        } else if(C == '/') {
          T /= N;
        }
      }
    } else {
      scanf("%s", &C);
    }

    if(C == '=') {
      break;
    }

    is_num ^= 1;
  }

  printf("%d\n", T);

  return 0;
}
