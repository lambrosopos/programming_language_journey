#include <stdio.h>

int main(int argc, char *argv[]) {
  int T;
  int W, H;
  int total=0;

  scanf("%d", &T);

  int i;
  for(i=0; i<T; i++) {
    scanf("%d %d", &W, &H);

    if(W == 136) {
      total+=1000;
    } else if (W == 142) {
      total+=5000;
    } else if (W == 148) {
      total+=10000;
    } else if (W == 154) {
      total+=50000;
    }
  }

  printf("%d\n", total);
}
