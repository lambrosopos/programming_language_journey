#include <stdio.h>

int main(int argc, char *argv[]) {
  int distance_secs;
  int total_secs=0;
  int i;
  for(i=0; i<4; i++) {
    scanf("%d", &distance_secs);
    total_secs+=distance_secs;
  }
  
  printf("%d\n", total_secs/60);
  printf("%d\n", total_secs%60);

  return 0;
}
