#include <stdio.h>

int main(int argc, char *argv[]) {
  int S;
  int socks[10]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

  for(int i=0; i<5; i++) {
    scanf("%d", &S);

    socks[S]+=1;
  }

  for(int i=0; i<10; i++) {
    if(socks[i] % 2) {
      printf("%d\n", i);
      break;
    }
  }

  return 0;
}
