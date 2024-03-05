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

  int recv_cnt;
  int recv_len;
  int filename_sz;
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

    // Need filename size using single byte => 2**8
    filename_sz=0;
    read(clnt_sock, &filename_sz, 1);

    // Get filename string
    recv_len=0;
    while(recv_len < filename_sz-1) {
      recv_cnt=read(clnt_sock, &filename, filename_sz);
      recv_len+=recv_cnt;
    }

    printf("Received filename size : %d\n", filename_sz);
    printf("Received filename : %s\n", filename);

    if((file_ptr=fopen(filename, "r"))==NULL){
      printf("No file\n");
    } else {
      while(fgets(line, BUF_SIZE, file_ptr) != NULL) {
        printf("Sending line: %s\n", line);
        write(clnt_sock, line, BUF_SIZE);
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
