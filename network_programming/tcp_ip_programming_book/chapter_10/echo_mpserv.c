#include <netinet/in.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/wait.h>

#define BUF_SIZE 30

void error_handling(char *message);
void read_childproc(int sig);

int main(int argc, char *argv[]) {
  int serv_sd, clnt_sd;
  struct sockaddr_in serv_adr, clnt_adr;
  socklen_t adr_sz;

  int str_len;
  char buf[BUF_SIZE];

  pid_t pid;
  int state;
  struct sigaction act;

  if(argc != 2) {
    printf("Usage : %s <PORT>\n", argv[0]);
    exit(1);
  }

  act.sa_handler=read_childproc;
  sigemptyset(&act.sa_mask);
  act.sa_flags=0;

  state=sigaction(SIGCHLD, &act, 0);

  serv_sd=socket(PF_INET, SOCK_STREAM, 0);
  memset(&serv_adr, 0, sizeof(serv_adr));
  serv_adr.sin_family=AF_INET;
  serv_adr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_adr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sd, (struct sockaddr*) &serv_adr, sizeof(serv_adr)) == -1) {
    error_handling("bind() error");
  } else {
    printf("bind() success\n");
  }

  if(listen(serv_sd, 5) == -1) {
    error_handling("listen() error");
  } else {
    printf("listen() success\n");
  }

  while(1) {
    adr_sz=sizeof(clnt_adr);
    clnt_sd=accept(serv_sd, (struct sockaddr*) &clnt_adr, &adr_sz);

    if(clnt_sd == -1) {
      continue;
    } else {
      printf("New client connected...\n");
    }

    pid=fork();
    if(pid == -1) {
      close(clnt_sd);
      continue;
    }

    if(pid == 0) {
      // Child process
      close(serv_sd);

      while((str_len=read(clnt_sd, buf, BUF_SIZE)) != 0) {
        write(clnt_sd, buf, str_len);
      }

      close(clnt_sd);
      puts("Client disconnected...");
      return 0;
    } else {
      // Parent process
      close(clnt_sd);
    }
  }

  close(serv_sd);
  return 0;
}

void read_childproc(int sig) {
  pid_t pid;
  int status;
  pid=waitpid(-1, &status, WNOHANG);
  printf("removed proc id: %d \n", pid);
}

void error_handling(char *message) {
  fputs(message, stderr);
  fputc('\n', stderr);
  exit(1);
}
