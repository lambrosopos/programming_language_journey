#include <stdio.h>

int main(int argc, char *argv[]) {
  int N;
  int total=91;

  scanf("%d", &N);
  total+=N;
  scanf("%d", &N);
  total+=N*3;
  scanf("%d", &N);
  total+=N;

  printf("The 1-3-sum is %d\n", total);

  return 0;
}
