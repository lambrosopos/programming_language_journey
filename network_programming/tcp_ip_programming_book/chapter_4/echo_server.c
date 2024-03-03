#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h> #include <sys/socket.h>
#include <unistd.h>

#define BUF_SIZE 5

void error_handling(char* message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char* argv[]) {
  int clnt_sock, serv_sock;
  struct sockaddr_in serv_addr, clnt_addr;
  socklen_t clnt_addr_sz;
  char message[BUF_SIZE];
  int str_len;

  if(argc != 2) {
    printf("Usage : %s <PORT>\n", argv[0]);
  } else {
    printf("Using port: %s\n", argv[1]);
  }

  int port_num = atoi(argv[1]);

  serv_sock=socket(PF_INET, SOCK_STREAM, 0);
  if(serv_sock == -1) {
    error_handling("socket() error");
  }

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_addr.sin_port=htons(port_num);

  if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("bind() error");
  }
  
  if(listen(serv_sock, 5) == -1) {
    error_handling("listen() error");
  }

  clnt_addr_sz=sizeof(clnt_addr);

  int i;
  for(i=0; i<5; i++) {
    clnt_sock=accept(serv_sock, (struct sockaddr*) &clnt_addr, &clnt_addr_sz);
    if(clnt_sock == -1) {
      error_handling("accept() error");
    } else {
      printf("Connected to client %d \n", i+1);
    }

    while((str_len=read(clnt_sock, message, BUF_SIZE)) != 0) {
      printf("Received message from client: %d\n Message: %s\n", i+1, message);
      write(clnt_sock, message, str_len);
    }

    close(clnt_sock);
  }

  close(serv_sock);
  return 0;
}
