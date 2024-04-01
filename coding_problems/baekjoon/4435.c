#include <stdio.h>

void solve();

int main(int argc, char *argv[]) {
  int N;

  scanf("%d", &N);
  getchar();
  
  for(int i=0; i<N; i++) {
    solve();
  }
}

void solve() {
  int G[6]={1, 2, 3, 3, 4, 10};
  int S[7]={1, 2, 2, 2, 3, 5, 10};

  int N;
  int total;
  int i;

  for(i=0; i<6; i++) {
    scanf("%d", &N);
    total+=N*G[i];
  }

  for(i=0; i<7; i++) {
    scanf("%d", &N);
    total-=N*S[i];
  }

  printf("%d\n", total);
}
