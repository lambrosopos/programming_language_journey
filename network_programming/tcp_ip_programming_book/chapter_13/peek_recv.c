#include <netinet/in.h>
#include <stdio.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdlib.h>

#define BUF_SIZE 30

void error_handling(char *message);

int main(int argc, char *argv[]) {
  int acpt_sock, recv_sock;
  struct sockaddr_in acpt_adr, recv_adr;
  int str_len, state;
  socklen_t adr_sz;
  char buf[BUF_SIZE];

  if(argc != 2) {
    printf("Usage : %s <port>\n", argv[0]);
    exit(1);
  }

  acpt_sock=socket(PF_INET, SOCK_STREAM, 0);
  memset(&acpt_adr, 0, sizeof(acpt_adr));
  acpt_adr.sin_family=AF_INET;
  acpt_adr.sin_addr.s_addr=htonl(INADDR_ANY);
  acpt_adr.sin_port=htons(atoi(argv[1]));

  if(bind(acpt_sock, (struct sockaddr*) &acpt_adr, sizeof(acpt_adr)) == -1) {
    error_handling("bind() error");
  }

  if(listen(acpt_sock, 5) == -1) {
    error_handling("listen() error");
  }

  adr_sz=sizeof(recv_adr);
  recv_sock=accept(acpt_sock, (struct sockaddr*) &recv_adr, &adr_sz);

  while(1) {
    str_len=recv(recv_sock, buf, sizeof(buf)-1, MSG_PEEK|MSG_DONTWAIT); // read message but, doesn't erase from socket. dontwait -> nonblocking
    if(str_len > 0) {
      break;
    }
  }

  buf[str_len]=0;
  printf("Buffering %d bytes : %s\n", str_len, buf);

  str_len=recv(recv_sock, buf, sizeof(buf)-1, 0);

  buf[str_len]=0;
  printf("Read again : %s\n", buf);

  close(recv_sock);
  close(acpt_sock);

  return 0;
}

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}
