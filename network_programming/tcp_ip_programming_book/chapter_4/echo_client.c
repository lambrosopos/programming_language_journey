#include <arpa/inet.h>
#include <stdlib.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define BUF_SIZE 5

void error_handling(char* message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char* argv[]) {
  int client_socket;
  struct sockaddr_in serv_addr;
  char message[BUF_SIZE];
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
    printf("Connected...");
  }

  while(1) {
    fputs("Input meessage(Q to quit): ", stdout);
    fgets(message, BUF_SIZE, stdin);

    if(!strcmp(message, "q\n") || !strcmp(message, "Q\n")) {
      break;
    }

    fputc('\n', stdout);

    write(client_socket, message, strlen(message));

    while(1) {
      str_len=read(client_socket, message, BUF_SIZE-1);
      printf("str_len: %d", str_len);
      if(str_len <= 0) {
        break;
      }
      message[str_len]=0;
      printf("Message from server : %s\n", message);
    }
  }
  close(client_socket);
  return 0;
}
