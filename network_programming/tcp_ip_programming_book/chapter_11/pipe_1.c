#include <stdio.h>
#include <unistd.h>

#define BUF_SIZE 30

int main(int argc, char *argv[]) {
  int fds[2]; // file descriptors for handling pipe input/output
  char str[]="Who are you?";
  char buf[BUF_SIZE];

  pid_t pid;

  pipe(fds); // fds[1] => output fds[0] => input
  pid=fork();

  if(pid == 0) {
    write(fds[1], str, sizeof(str));
  } else {
    read(fds[0], buf, BUF_SIZE);
    puts(buf);
  }

  return 0;
}
