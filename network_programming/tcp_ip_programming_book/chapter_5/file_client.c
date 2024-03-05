#include <stdlib.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 1024
#define FILENAME_SZ 32

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int sock;
  int filename_sz;
  struct sockaddr_in serv_addr;

  int read_cnt;
  char filename[FILENAME_SZ];
  char line[BUF_SIZE];

  if(argc != 3) {
    printf("Usage : %s <ip> <port>", argv[0]);
  }

  sock=socket(PF_INET, SOCK_STREAM, 0);

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=inet_addr(argv[1]);
  serv_addr.sin_port=htons(atoi(argv[2]));

  if(connect(sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("connect() error");
  } else {
    printf("Connected to %s:%s\n", argv[1], argv[2]);
  }

  printf("Enter filename : ");
  scanf("%s", filename);
  printf("\n");

  write(sock, filename, strlen(filename)+1);

  while((read_cnt=read(sock, line, BUF_SIZE) != 0)) {
    printf("%s", line);
  }

  close(sock);
  return 0;
}
