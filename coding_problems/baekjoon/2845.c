#include <stdio.h>

int main(int argc, char *argv[]) {
  int num_per_m;
  int m_square;
  int T;

  int A, B, C, D, E;

  scanf("%d %d", &num_per_m, &m_square);
  scanf("%d %d %d %d %d", &A, &B, &C, &D, &E);

  T=num_per_m * m_square;
  printf("%d %d %d %d %d\n", A-T, B-T, C-T, D-T, E-T);

  return 0;
}
