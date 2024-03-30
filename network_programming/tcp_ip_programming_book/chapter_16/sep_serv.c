#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>  

#define BUF_SIZE 1024

int main(int argc, char *argv[]) {
  int serv_sock, clnt_sock;
  FILE *readfp;
  FILE *writefp;

  struct sockaddr_in serv_adr, clnt_adr;
  socklen_t adr_sz;
  char buf[BUF_SIZE]={0,};

  serv_sock=socket(PF_INET, SOCK_STREAM, 0);
  memset(&serv_adr, 0, sizeof(serv_adr));
  serv_adr.sin_family=AF_INET;
  serv_adr.sin_addr.s_addr=inet_addr(argv[1]);
  serv_adr.sin_port=htons(atoi(argv[2]));

  if(bind(serv_sock, (struct sockaddr*) &serv_adr, sizeof(serv_adr)) == -1) {
    printf("bind() error\n");
    exit(1);
  }

  listen(serv_sock, 5);

  adr_sz=sizeof(clnt_adr);
  clnt_sock=accept(serv_sock, (struct sockaddr*) &clnt_adr, &adr_sz);

  readfp=fdopen(clnt_sock, "r");
  writefp=fdopen(dup(clnt_sock), "w");

  fputs("FROM Server: Hi~ client? \n", writefp);
  fputs("I love all of the world \n", writefp);
  fputs("You are awesome! \n", writefp);
  fflush(writefp);

  shutdown(fileno(writefp), SHUT_WR);
  fclose(writefp);

  fgets(buf, sizeof(buf), readfp);
  fputs(buf, stdout);
  fclose(readfp);

  return 0;
}
