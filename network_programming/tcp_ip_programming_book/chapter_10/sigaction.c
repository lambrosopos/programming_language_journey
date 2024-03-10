#include <stdio.h>
#include <unistd.h>
#include <signal.h>

void timeout(int sig) {
  if(sig == SIGALRM) {
    puts("Time out!");
  }

  alarm(2);
}

int main(int argc, char *argv[]) {
  int i;
  struct sigaction act;

  // Registering signal handler
  act.sa_handler=timeout;

  // Initializing default values to 0
  // memset(&act.sa_mask, 0, sizeof(act.sa_mask)); -- need <string.h>
  sigemptyset(&act.sa_mask); // easier way of setting t 0

  act.sa_flags=0;
  sigaction(SIGALRM, &act, 0);

  // Sending sigalrm signal in 2 seconds;
  alarm(2);

  for(i=0; i<3; i++) {
    puts("wait...");
    sleep(100);
  }

  return 0;
}
