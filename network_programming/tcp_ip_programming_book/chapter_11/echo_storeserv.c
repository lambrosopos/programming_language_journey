#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <unistd.h>
#include <string.h>

#define BUF_SIZE 128

void error_handling(char *message);
void read_childproc(int sig);

int main(int argc, char *argv[]) {
  int serv_sd, clnt_sd;
  struct sockaddr_in serv_adr, clnt_adr;
  socklen_t adr_size;

  char buf[BUF_SIZE];

  int str_len;
  // For multiprocessing
  pid_t pid;
  int state;
  struct sigaction act;
  int fds[2];

  if(argc != 2) {
    printf("Usage : %s <PORT>\n", argv[0]);
    exit(1);
  }

  serv_sd=socket(PF_INET, SOCK_STREAM, 0);

  memset(&serv_adr, 0, sizeof(serv_adr));
  serv_adr.sin_family=AF_INET;
  serv_adr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_adr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sd, (struct sockaddr*) &serv_adr, sizeof(serv_adr)) == -1) {
    error_handling("bind() error");
  }

  if(listen(serv_sd, 5) == -1) {
    error_handling("listen() error");
  }

  act.sa_handler=read_childproc;
  sigemptyset(&act.sa_mask);
  act.sa_flags=0;
  state=sigaction(SIGCHLD, &act, 0);

  pipe(fds);
  pid=fork();
  if(pid == 0) {
    FILE *fp=fopen("echomsg.txt", "wt");

    char msgbuf[BUF_SIZE];
    int i, len;

    for(i=0; i<10; i++) {
      len=read(fds[0], msgbuf, BUF_SIZE);
      fwrite((void*) msgbuf, 1, len, fp);
    }

    fclose(fp);
    return 0;
  }

  int clnt_no=0;
  while(1) {
    adr_size=sizeof(clnt_adr);
    clnt_sd=accept(serv_sd, (struct sockaddr*) &clnt_adr, &adr_size);

    clnt_no++;

    if(clnt_sd == -1) {
      printf("accept() error for client %d\n", clnt_no);
      continue;
    }

    printf("connected to client %d\n", clnt_no);

    pid=fork();
    if(pid == 0) {
      close(serv_sd);

      while((str_len=read(clnt_sd, buf, BUF_SIZE)) != 0) {
        write(clnt_sd, buf, str_len);
        write(fds[1], buf, str_len);
      }

      close(clnt_sd);
      printf("disconnected from client : %d\n", clnt_no);
      return 0;
    } else {
      close(clnt_sd);
    }

  }
  close(serv_sd);
  return 0;
}

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}

void read_childproc(int sig) {
  pid_t pid;
  int status;
  pid=waitpid(-1, &status, WNOHANG);
  printf("removed proc id: %d \n", pid);
}

