#include <stdlib.h>
#include <stdio.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 30

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int serv_sock;
  socklen_t clnt_addr_sz;
  struct sockaddr_in serv_addr;
  struct sockaddr_in clnt_addr;

  char message[BUF_SIZE];

  if(argc != 2) {
    printf("Usage : %s <port>\n", argv[1]);
    exit(1);
  }

  serv_sock=socket(PF_INET, SOCK_DGRAM, 0);

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_addr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("bind() error");
  }

  while(1) {
    clnt_addr_sz=sizeof(clnt_addr);
    recvfrom(serv_sock, message, BUF_SIZE-1, 0, (struct sockaddr*) &clnt_addr, &clnt_addr_sz);
    sendto(serv_sock, message, strlen(message), 0, (struct sockaddr*) &clnt_addr, clnt_addr_sz);
  }

  close(serv_sock);
  return 0;
}
