#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

#define BUF_SIZE 30

void read_childproc(int sig);

int main(int argc, char *argv[]) {
  int i;
  int str_len;
  char message[BUF_SIZE];

  // Multiprocessing
  pid_t pid;
  int state;
  int fds_1[2];
  int fds_2[2];

  struct sigaction act;

  act.sa_handler=read_childproc;
  sigemptyset(&act.sa_mask);
  act.sa_flags=0;
  state=sigaction(SIGCHLD, &act, 0);

  // Create pipes
  pipe(fds_1);
  pipe(fds_2);

  pid=fork();
  if(pid == 0) {
    for(i=0; i<3; i++) {
      str_len=read(fds_1[0], message, BUF_SIZE);
      printf("Child proc : %s\n", message);
      write(fds_2[1], message, str_len);
    }

    return 0;
  } else {
    write(fds_1[1], "hello", 5);

    for(i=0; i<3; i++) {
      str_len=read(fds_2[0], message, BUF_SIZE);
      printf("Parent proc : %s\n", message);
      write(fds_1[1], message, str_len);
    }
  }

  return 0;
}

void read_childproc(int sig) {
  pid_t pid;
  int status;
  pid=waitpid(-1, &status, WNOHANG);
  printf("removed proc id: %d \n", pid);
}
