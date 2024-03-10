#include <stdio.h>
#include <unistd.h>

int gval=10;

int main(int argc, char *argv[]) {
  pid_t pid;
  int lval=10;

  // Increase values
  gval++, lval+=5;

  pid=fork();
  if(pid == 0) {
    // Forked process
    gval+=2, lval +=2;
  } else {
    // parent process
    gval-=2, lval -=2;
  }

  if(pid == 0) {
    printf("Child process: [%d, %d] \n", gval, lval);
  } else {
    printf("Parent process: [%d, %d] \n", gval, lval);
  }

  return 0;
}
