#include <asm-generic/socket.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/socket.h>

#define BUF_SIZE 1024

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int sock;
  int snd_buf=BUF_SIZE;
  int rcv_buf=BUF_SIZE*3;
  int state;
  socklen_t len;

  sock=socket(PF_INET, SOCK_STREAM, 0);

  // Set socket input/output buffer sizes
  state=setsockopt(sock, SOL_SOCKET, SO_RCVBUF, (void *) &rcv_buf, sizeof(rcv_buf));
  if(state == -1)
    error_handling("setsockopt() error");
  printf("Set input buffer to : %d\n", rcv_buf);

  state=setsockopt(sock, SOL_SOCKET, SO_SNDBUF, (void *) &snd_buf, sizeof(snd_buf));
  if(state == -1)
    error_handling("setsockopt() error");
  printf("Set output buffer to : %d\n", snd_buf);

  // Get socket input/output buffer sizes
  len=sizeof(rcv_buf);
  state=getsockopt(sock, SOL_SOCKET, SO_RCVBUF, (void *) &rcv_buf, &len);
  if(state == -1)
    error_handling("getsockopt() error");
  printf("Get input buffer size : %d\n", rcv_buf);

  len=sizeof(snd_buf);
  state=getsockopt(sock, SOL_SOCKET, SO_SNDBUF, (void *) &snd_buf, &len);
  if(state == -1)
    error_handling("getsockopt() error");
  printf("Get output buffer size : %d\n", snd_buf);

  return 0;
}
