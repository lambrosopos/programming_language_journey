#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 30

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int sock;
  char message[BUF_SIZE];
  int str_len;
  struct sockaddr_in serv_addr;
  struct sockaddr_in from_addr;
  socklen_t addr_sz;

  if(argc != 3) {
    printf("Usage : %s <ip> <port>\n", argv[0]);
  }

  sock=socket(PF_INET, SOCK_DGRAM, 0);

  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=inet_addr(argv[1]);
  serv_addr.sin_port=htons(atoi(argv[2]));

  // UDP sockets are unconnected by default.
  // Unconnected sockets register IP and PORT info on sendto
  // They also remove registered information after sendto is finished.
  //
  // This operation takes around 30% of resources.
  //
  // Connected sockets register IP and PORT to a socket, so the above process doesn't get repeated.
  //
  // This is useful when UDP sockets are contacting same host.
  
  if(connect(sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("connect() error");
  }

  while(1) {
    fputs("Insert message (q to quit) : ", stdout);
    fgets(message, sizeof(message), stdin);

    if(!strcmp(message, "q\n") || !strcmp(message, "Q\n")) {
      break;
    }

    // Unconnected UDP sockets.
    /*
    sendto(sock, message, strlen(message), 0, (struct sockaddr*) &serv_addr, sizeof(serv_addr));
    addr_sz=sizeof(from_addr);
    str_len=recvfrom(sock, message, BUF_SIZE, 0, (struct sockaddr*) &from_addr, &addr_sz);
    */

    // Connected sockets can simply use read/write since destinations are fixed.
    write(sock, message, strlen(message));
    read(sock, message, BUF_SIZE);


    message[str_len]=0;
    printf("Message from server : %s\n", message);
  }

  close(sock);

  return 0;
}
