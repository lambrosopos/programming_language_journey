#include <stdio.h>

int convert_to_seconds(int hour, int minutes) {
  return hour*3600 + minutes*60;
}

void solve() {
  int s_hr;
  int s_min;
  int s_sec;

  int e_hr;
  int e_min;
  int e_sec;

  int f_hr;
  int f_min;
  int total_secs;

  scanf("%d %d %d %d %d %d", &s_hr, &s_min, &s_sec, &e_hr, &e_min, &e_sec);

  total_secs=e_sec-s_sec;
  total_secs-=convert_to_seconds(s_hr, s_min);
  total_secs+=convert_to_seconds(e_hr, e_min);

  f_hr=total_secs/3600;
  total_secs-=f_hr*3600;
  
  f_min=total_secs/60;
  total_secs-=f_min*60;

  printf("%d %d %d\n", f_hr, f_min, total_secs);
}

int main(int argc, char *argv[]) {
  int i;

  for(i=0; i<3; i++) {
    solve();
  }

  return 0;
}
