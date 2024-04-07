#include <stdio.h>

int solve();

int main(int argc, char *argv[]) {
  int N;

  scanf("%d", &N);
  getchar();
  
  for(int i=0; i<N; i++) {
    int total=solve();

    if(total > 0) {
      printf("Battle %d: Good triumphs over Evil\n", i+1);
    } else if(total < 0) {
      printf("Battle %d: Evil eradicates all trace of Good\n", i+1);
    } else {
      printf("Battle %d: No victor on this battle field\n", i+1);
    }
  }
}

int solve() {
  int G[6]={1, 2, 3, 3, 4, 10};
  int S[7]={1, 2, 2, 2, 3, 5, 10};

  int N;
  int total=0;
  int i;

  for(i=0; i<6; i++) {
    scanf("%d", &N);
    total+=N*G[i];
  }

  for(i=0; i<7; i++) {
    scanf("%d", &N);
    total-=N*S[i];
  }
    
  return total;
}
