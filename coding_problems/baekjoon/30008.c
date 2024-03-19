#include <stdio.h>

int main(int argc, char *argv[]) {
  int N, K;

  scanf("%d %d", &N, &K);

  int G[K];
  int H[K];

  int i=0;
  while(i < K) {
    scanf("%d", &G[i++]);
  }

  i=0;
  int grade;
  while(i < K) {
    grade=100*G[i]/N;

    if(grade >= 0 && grade <= 4) {
      H[i]=1;
    } else if(grade > 4 && grade <= 11) {
      H[i]=2;
    } else if(grade > 11 && grade <= 23) {
      H[i]=3;
    } else if(grade > 23 && grade <= 40) {
      H[i]=4;
    } else if(grade > 40 && grade <= 60) {
      H[i]=5;
    } else if(grade > 60 && grade <= 77) {
      H[i]=6;
    } else if(grade > 77 && grade <= 89) {
      H[i]=7;
    } else if(grade > 89 && grade <= 96) {
      H[i]=8;
    } else if(grade > 96 && grade <= 100) {
      H[i]=9;
    }

    i++;
  }

  i=0;
  while(i < K) {
    printf("%d", H[i++]);
    printf(i < K ? " " : "\n");
  }

  return 0;
}
