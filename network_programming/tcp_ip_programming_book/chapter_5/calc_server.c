#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define BUF_SIZE 1024
#define OPSZ 4

void error_handling(char *message);
int calculate(int opnum, int opnds[], char operator);

int main(int argc, char* argv[])
{
  // Basic server info
  int serv_sock;
  int clnt_sock;
  socklen_t clnt_adr_size;
  struct sockaddr_in serv_addr;
  struct sockaddr_in clnt_addr;

  // Operator information
  int i;
  int opnd_cnt;
  int recv_len;
  int recv_cnt;
  int result;
  char operator;
  char opinfo[BUF_SIZE];

  if(argc != 2) {
    printf("Usage : %s <PORT>\n", argv[0]);
    exit(1);
  }

  // Create socket
  serv_sock=socket(PF_INET, SOCK_STREAM, 0);

  // Bind to port
  memset(&serv_addr, 0, sizeof(serv_addr));
  serv_addr.sin_family=AF_INET;
  serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
  serv_addr.sin_port=htons(atoi(argv[1]));

  if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1) {
    error_handling("bind() error");
  } else {
    printf("binded to %d:%d\n", INADDR_ANY, atoi(argv[1]));
  }

  if(listen(serv_sock, 5) == -1) {
    error_handling("listen() error");
  } else {
    printf("Listening on port %s\n", argv[1]);
  }

  clnt_adr_size=sizeof(clnt_addr);

  for(i=0; i<5; i++) {
    opnd_cnt=0;
    clnt_sock=accept(serv_sock, (struct sockaddr*) &clnt_addr, &clnt_adr_size);
    read(clnt_sock, &opnd_cnt, 1);

    recv_len=0;

    // 여기에서 operator 까지 읽어오기
    while(recv_len < (opnd_cnt*OPSZ+1)) { 
      recv_cnt = read(clnt_sock, &opinfo[recv_len], BUF_SIZE-1);
      recv_len += recv_cnt;
    }

    result=calculate(opnd_cnt, (int*)opinfo, opinfo[recv_len-1]);
    write(clnt_sock, &result, sizeof(result));
    close(clnt_sock);
  }

  close(serv_sock);
  printf("Closed server\n");
  return 0;
}

void error_handling(char *message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}

int calculate(int opnum, int opnds[], char op) {
  int result = opnds[0];
  int i;
  switch(op) {
    case '+':
      for(i=1; i<opnum; i++) result+=opnds[i];
      break;
    case '*':
      for(i=1; i<opnum; i++) result*=opnds[i];
      break;
    case '-':
      for(i=1; i<opnum; i++) result-=opnds[i];
      break;
  }

  return result;
}
