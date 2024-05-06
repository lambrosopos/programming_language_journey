#include <stdio.h>

int main(int argc, char *argv[]) {
  int H, M;

  scanf("%d %d", &H, &M);

  printf("%d\n", (H-9) * 60 + M);

  return 0;
}
