#include <stdio.h>

void solve();

int main(int argc, char *argv[]) {
  int T;
  int i;

  scanf("%d", &T);

  for(i=0; i<T; i++) {
    solve();
  }
}

void solve(){
  int G;
  int C;
  int E;

  int rem;
  int kilos;

  scanf("%d %d %d", &G, &C, &E);

  rem=E-C;

  if(rem <= 0){
    printf("0\n");
    return;
  }

  if(G == 1){
    kilos=rem*G;
  } else if(G == 2) {
    kilos=rem*3;
  } else if(G == 3) {
    kilos=rem*5;
  }

  printf("%d\n", kilos);
}
