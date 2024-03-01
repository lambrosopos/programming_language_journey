#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int server_socket;
  int client_socket;

  struct sockaddr_in server_address;
  struct sockaddr_in client_address;
  socklen_t client_address_size;

  char message[]="Hello World!";

  if(argc!=2) {
    printf("Usage :%s <port>\n", argv[0]);
    exit(1);
  } else {
    printf("Using PORT: %s\n", argv[1]);
  }

  int port_num = atoi(argv[1]);

  server_socket=socket(PF_INET, SOCK_STREAM, 0);
  if(server_socket == -1) {
    error_handling("socket() error");
  } else {
    printf("Allocated file descriptor: %d\n", server_socket);
  }

  memset(&server_address, 0, sizeof(server_address));
  server_address.sin_family=AF_INET;
  server_address.sin_addr.s_addr=htonl(INADDR_ANY);
  server_address.sin_port=htons(port_num);

  if(bind(server_socket, (struct sockaddr*) &server_address, sizeof(server_address)) == -1) {
    error_handling("bind()");
  } else {
    printf("Address binded to: %d\n", PF_INET);
  }

  if(listen(server_socket, 5) == -1) {
    error_handling("listen() error");
  } else {
    printf("Listening on port: %d\n", port_num);
  }


  client_address_size=sizeof(client_address_size);
  client_socket=accept(server_socket, (struct sockaddr*) &client_address, &client_address_size);
  if(client_socket == -1){
    error_handling("accept() error");
  } else {
    printf("Accepted client socket: %d\n", client_socket);
  }

  write(client_socket, message, sizeof(message));
  close(client_socket);
  close(server_socket);

  return 0;
}

