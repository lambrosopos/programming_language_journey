#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

#define BUF_SIZE 30

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int serv_sock;
  int clnt_sock;
  socklen_t clnt_addr_sz;
  struct sockaddr_in serv_addr;
  struct sockaddr_in clnt_addr;

  char message[BUF_SIZE];

  int read_cnt;
  FILE *fp;

  if(argc != 2) {
    printf("Usage : %s <port>\n", argv[0]);
    exit(1);
  }

  serv_sock=socket(PF_INET, SOCK_STREAM, 0);

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_addr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("bind() error");
  }

  if(listen(serv_sock, 5) == -1) {
    error_handling("listen() error");
  }

  clnt_addr_sz=sizeof(clnt_addr);
  clnt_sock=accept(serv_sock, (struct sockaddr*) &clnt_addr, &clnt_addr_sz);

  fp=fopen("example.txt", "rt");

  while(1) {
    read_cnt=fread((void*) message, 1, BUF_SIZE, fp);
    if(read_cnt < BUF_SIZE) {
      write(clnt_sock, message, read_cnt);
      break;
    }
    write(clnt_sock, message, BUF_SIZE);
  }

  shutdown(clnt_sock, SHUT_WR);

  read(clnt_sock, message, BUF_SIZE);
  printf("Message from client : %s\n", message);

  fclose(fp);
  close(clnt_sock);
  close(serv_sock);

  return 0;
}
