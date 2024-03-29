#include <stdio.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>

#define BUF_SIZE 3
// #define BUF_SIZE 4096 //buffering for fputs is usually few kb. if buf_size is adquate, it performs better

int main(int argc, char *argv[]) {
  clock_t start=clock();
  int fd1, fd2;
  int len;
  char buf[BUF_SIZE];

  fd1 = open("news.txt", O_RDONLY);
  fd2 = open("cpy.txt", O_WRONLY|O_CREAT|O_TRUNC);

  while((len=read(fd1, buf, sizeof(buf))) > 0) {
    write(fd2, buf, len);
  }

  close(fd1);
  close(fd2);

  clock_t end=clock();
  float seconds=(float)(end-start)/CLOCKS_PER_SEC;

  printf("%f", seconds);

  return 0;
}
