#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>

#define BUF_SIZE 1024
#define FILENAME_SIZE 32

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int serv_sock;
  int clnt_sock;
  struct sockaddr_in serv_addr;
  struct sockaddr_in clnt_addr;
  socklen_t clnt_addr_sz;

  char filename[FILENAME_SIZE];

  // File operations
  FILE *file_ptr;
  char line[BUF_SIZE];

  if(argc != 2) {
    printf("Usage : %s <port>\n", argv[0]);
  }

  serv_sock = socket(PF_INET, SOCK_STREAM, 0);

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_addr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("bind() error");
  } else {
    printf("Bind success\n");
  }

  if(listen(serv_sock, 5) == -1) { error_handling("listen() error");
  } else {
    printf("Listening on port : %s\n", argv[1]);
  }

  while(1) {
    clnt_addr_sz=sizeof(clnt_addr);

    // Connect to client socket
    clnt_sock=accept(serv_sock, (struct sockaddr*) &clnt_addr, &clnt_addr_sz);
    printf("Connected to client...\n");

    // Get filename string
    read(clnt_sock, filename, FILENAME_SIZE);

    printf("Received filename : %s\n", filename);

    int line_cnt;
    if((file_ptr=fopen(filename, "r"))==NULL){
      printf("File not found: %s\n", filename);
    } else {
      while(1) {
        line_cnt=fread(line, 1, BUF_SIZE, file_ptr);
        if(line_cnt<BUF_SIZE) {
          write(clnt_sock, line, line_cnt);
          break;
        }
        write(clnt_sock, line, line_cnt);
      }
    }

    // Close used sockets
    close(clnt_sock);
    printf("Closing client socket...\n");

    fputc('\n', stdout);
  }

  close(serv_sock);

  return 0;
}
