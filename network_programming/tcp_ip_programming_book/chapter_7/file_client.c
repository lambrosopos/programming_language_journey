#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>

#define BUF_SIZE 30

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int sd;
  struct sockaddr_in serv_addr;

  int read_cnt;
  char message[BUF_SIZE];

  FILE *fp;

  if(argc != 3) {
    printf("Usage : %s <ip> <port>", argv[0]);
    exit(1);
  }

  fp=fopen("example_2.txt", "wt");
  sd=socket(PF_INET, SOCK_STREAM, 0);
  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=inet_addr(argv[1]);
  serv_addr.sin_port=htons(atoi(argv[2]));

  if(connect(sd, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("connect() error");
  }

  while((read_cnt=read(sd, message, BUF_SIZE)) != 0) {
    fwrite((void*) message, 1, read_cnt, fp);
  }

  puts("Received file data");

  write(sd, "Thank You", 10);

  close(sd);

  return 0;
}
