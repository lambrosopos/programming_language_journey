#include <stdio.h>

int power(int base, int exp);
int round_digit(int number, int exp);

int main(int argc, char *argv[]) {
  int N;

  scanf("%d", &N);

  int i=1;
  while(N >= power(10, i)) {
    // Round the i-1 th digit
    // N = 125, i = 1
    // N >= 10^1
    // Round N i-1 th digit -> 0th digit from the right
    N=round_digit(N, i);
    i++;
  }

  printf("%d\n", N);

  return 0;
}

int power(int base, int exp) {
  if(exp == 0) {
    return 1;
  } else if(exp%2) {
    return base * power(base, exp-1);
  } else {
    int temp = power(base, exp/2);
    return temp * temp;
  }
}

int round_digit(int number, int exp) {
  double divided = (double)number / power(10, exp);
  int rounded = (int)(divided + 0.5);
  int result = rounded * power(10, exp);

  return result;
}
