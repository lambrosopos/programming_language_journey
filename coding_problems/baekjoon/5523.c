#include <stdio.h>

int main(int argc, char *argv[]) {
  int N;
  int A, B;

  scanf("%d", &N);

  int R[2] = {0, 0};
  for(int i=0; i<N; i++) {
    scanf("%d %d", &A, &B);

    if(A > B) {
      R[0]++;
    } else if (A < B) {
      R[1]++;
    }
  }

  printf("%d %d\n", R[0], R[1]);

  return 0;
}
