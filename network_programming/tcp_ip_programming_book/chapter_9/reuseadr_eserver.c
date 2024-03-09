#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

#define BUF_SIZE 1024

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int serv_sock, clnt_sock;
  struct sockaddr_in serv_adr, clnt_adr;
  socklen_t sock_len;

  char message[BUF_SIZE];
  int i;
  int read_cnt;

  if(argc != 2) {
    printf("Usage : %s <PORT>\n", argv[0]);
    exit(1);
  }

  serv_sock=socket(PF_INET, SOCK_STREAM, 0);

  memset(&serv_adr, 0, sizeof(serv_adr));
  serv_adr.sin_family=AF_INET;
  serv_adr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_adr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sock, (struct sockaddr*) &serv_adr, sizeof(serv_adr)) == -1) {
    error_handling("bind() error");
  }

  if(listen(serv_sock, 5) == -1) {
    error_handling("listen() error");
  }

  for(i=0; i<5; i++) {
    sock_len=sizeof(clnt_adr);
    clnt_sock=accept(serv_sock, (struct sockaddr*) &clnt_adr, &sock_len);
    if(clnt_sock == -1) {
      error_handling("accept() error");
    }

    while((read_cnt=read(clnt_sock, &message, BUF_SIZE)) != 0) {
      printf("Received message : %s\n", message);
      write(clnt_sock, &message, sizeof(message));
    }

    close(clnt_sock);
  }

  close(serv_sock);
}
