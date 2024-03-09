#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

int main(int argc, char *argv[]) {
  int i;
  struct hostent *host;
  struct sockaddr_in addr;

  if(argc != 2) {
    printf("Usage : %s <IP>\n", argv[0]);
    exit(1);
  }

  memset(&addr, 0, sizeof(addr));
  addr.sin_addr.s_addr=inet_addr(argv[1]);

  host=gethostbyaddr((char*) &addr.sin_addr, 4, AF_INET); // Some reason not working
  if(!host) {
    error_handling("gethost() error");
  }

  printf("Official Name : %s\n", host->h_name);
  for(i=0; host->h_aliases[i]; i++) {
    printf("Alias %d : %s\n", i, host->h_aliases[i]);
  }

  printf("Address type %d : %s\n", i, host->h_addrtype == AF_INET ? "IPv4" : "IPv6");

  for(i=0; host->h_addr_list[i]; i++) {
    printf("IP addr %d : %s\n", i, inet_ntoa(*(struct in_addr*) host->h_addr_list[i]));
  }

  return 0;
}
