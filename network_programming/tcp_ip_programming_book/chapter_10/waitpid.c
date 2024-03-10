#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
  int status;
  pid_t pid=fork();

  if(pid == 0) {
    sleep(15);
    return 24;
  } else {
    // If passing -1 to waitpid as pid, it selects a child process
    while(!waitpid(-1, &status, WNOHANG)) {
      sleep(3);
      puts("Sleep 3 secs.");
    }

    if(WIFEXITED(status)) {
      printf("Child send %d\n", WEXITSTATUS(status));
    }
  }

  return 0;
}
