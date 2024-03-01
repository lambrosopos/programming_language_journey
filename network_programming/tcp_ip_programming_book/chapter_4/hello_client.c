#include <arpa/inet.h>
#include <stdlib.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

void error_handling(char* message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char* argv[]) {
  int client_socket;
  struct sockaddr_in serv_addr;
  char message[30];
  int str_len;

  if(argc != 3) {
    printf("Usage : %s <IP> <port>\n", argv[0]);
    exit(1);
  }

  client_socket=socket(PF_INET, SOCK_STREAM, 0);
  if(client_socket == -1) {
    error_handling("socket() error");
  } else {
    printf("created socket\n");
  }

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=inet_addr(argv[1]);
  serv_addr.sin_port=htons(atoi(argv[2]));

  if(connect(client_socket, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("connect() error");
  } else {
    printf("connect success\n");
  }

  str_len=read(client_socket, message, sizeof(message)-1);
  if(str_len == -1) {
    error_handling("read() error");
  }

  printf("Message from server : %s\n", message);
  close(client_socket);
  return 0;
}
