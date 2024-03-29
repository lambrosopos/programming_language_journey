// Convert file descriptor -> file struct pointer
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>

int main(void) {
  FILE *fp;
  int fd;
  fd=open("news.txt", O_WRONLY|O_CREAT|O_TRUNC);

  if(fd == -1) {
    fputs("file open error", stdout);
    exit(1);
  }

  fp=fdopen(fd, "w");
  fputs("Network C programming\n", fp);
  fclose(fp); // closing through file pointer also closes the file descriptor since it points to the same file
  return 0;
}
