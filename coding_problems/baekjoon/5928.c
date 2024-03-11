#include <stdio.h>

int main(int argc, char *argv[]) {
  int day, hour, min;

  int start_time;
  int diff;

  scanf("%d %d %d", &day, &hour, &min);

  start_time=11*24*60 + 11*60 + 11;

  diff=day*24*60 + hour*60 + min - start_time;

  if(diff < 0) {
    printf("-1\n");
  } else {
    printf("%d\n", diff);
  }

  return 0;
}
