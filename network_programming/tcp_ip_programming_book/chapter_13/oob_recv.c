#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <string.h>
#include <signal.h>
#include <fcntl.h>

#define BUF_SIZE 30

void error_handling(char *message);
void urg_handler(int signo);

// Global for urg_handler to use as well
int acpt_sock;
int recv_sock;

int main(int argc, char *argv[]) {
  struct sockaddr_in serv_adr, clnt_adr;
  socklen_t adr_sz;
  int str_len, state;
  struct sigaction act;
  char buf[BUF_SIZE];

  if(argc != 2) {
    printf("Usage : %s <port>\n", argv[0]);
    exit(1);
  }

  // register urgent signal action
  act.sa_handler=urg_handler;
  sigemptyset(&act.sa_mask);
  act.sa_flags=0;

  acpt_sock=socket(PF_INET, SOCK_STREAM, 0);
  memset(&serv_adr, 0, sizeof(serv_adr));
  serv_adr.sin_family=AF_INET;
  serv_adr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_adr.sin_port=htons(atoi(argv[1]));

  if(bind(acpt_sock, (struct sockaddr*) &serv_adr, sizeof(serv_adr)) == -1) {
    error_handling("bind() error");
  }

  if(listen(acpt_sock, 5) == -1) {
    error_handling("listen() error");
  }

  adr_sz=sizeof(clnt_adr);
  recv_sock=accept(acpt_sock, (struct sockaddr*) &clnt_adr, &adr_sz);

  fcntl(recv_sock, F_SETOWN, getpid());
  state=sigaction(SIGURG, &act, 0);

  // Regular receiving handling
  while((str_len=recv(recv_sock, buf, BUF_SIZE, 0)) != 0) {
    if(str_len == -1) {
      continue;
    }
    buf[str_len]=0;
    puts(buf);
  }

  close(recv_sock);
  close(acpt_sock);

  return 0;
}

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

void urg_handler(int signo) {
  int str_len;
  char buf[BUF_SIZE];

  str_len=recv(recv_sock, buf, sizeof(buf)-1, MSG_OOB);
  buf[str_len]=0;
  printf("Urgent message : %s\n", buf);
}
