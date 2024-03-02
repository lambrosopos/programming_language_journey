#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define BUF_SIZE 1024

void error_handling(char *message);

int main(int argc, char* argv[])
{
  // Basic server info
  int serv_sock;
  int clnt_sock;
  socklen_t clnt_sock_size;
  struct sockaddr_in serv_addr;
  struct sockaddr_in clnt_addr;

  if(argc != 2) {
    printf("Usage : %s <PORT>\n", argv[0]);
    exit(1);
  }

  // Create socket
  serv_sock=socket(PF_INET, SOCK_STREAM, 0);

  // Bind to port
  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_addr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("bind() error");
  } else {
    printf("binded to %d:%d\n", INADDR_ANY, atoi(argv[1]));
  }

  if(listen(serv_sock, 5) == -1) {
    error_handling("listen() error");
  } else {
    printf("Listening on port %s\n", argv[1]);
  }

  clnt_sock_size=sizeof(clnt_sock_size);
  clnt_sock=accept(serv_sock, (struct sockaddr*) &clnt_addr, &clnt_sock_size);

  write(clnt_sock, "hello\n", sizeof("hello\n"));

  close(serv_sock);
  printf("Closed server\n");
  return 0;
}

void error_handling(char *message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}

