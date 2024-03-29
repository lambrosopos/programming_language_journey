#include <stdio.h>

void solve() {
  int i;
  int N;

  int min=-1;
  int total=0;

  for(i=0; i<7; i++) {
    scanf("%d", &N);

    if(N%2 == 0) {
      total += N;

      if(min == -1) {
        min = N;
      } else if(N < min) {
        min = N;
      }
    }
  }

  printf("%d %d\n", total, min);
}

int main(int argc, char *argv[]) {
  int N;

  scanf("%d", &N);

  while(N--) {
    solve();
  }

  return 0;
}
