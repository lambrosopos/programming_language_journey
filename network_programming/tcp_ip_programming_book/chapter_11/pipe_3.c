#include <stdio.h>
#include <unistd.h>

#define BUF_SIZE 30

int main(int argc, char *argv[]) {
  int fds1[2];
  int fds2[2];
  pid_t pid;
  
  char buf[BUF_SIZE];
  char str1[]="Who are you?";
  char str2[]="Thank you for your message";

  pipe(fds1);
  pipe(fds2);

  pid=fork();

  if(pid == 0) {
    write(fds1[1], str1, sizeof(str1));
    read(fds2[0], buf, BUF_SIZE);
    printf("Child proc message : %s\n", buf);
  } else {
    write(fds2[1], str2, sizeof(str2));
    read(fds1[0], buf, BUF_SIZE);
    printf("Parent proc message : %s\n", buf);
  }

  return 0;
}
