#include <stdlib.h>
#include <stdio.h>
#include <arpa.inet.h>
#include <string.h>
#define BUF_SIZE 1024

void error_handling(char *message);

int main(int argc, char* argv[])
{
    // create server and client socket as integers since file descriptors will be returned to keep track
    int serv_sock, clnt_sock;
    // allocate message buffer size in advance
    char message[BUF_SIZE];

    // make a server and client socket address structs to conform to socket related functions
    struct sockaaddr_in serv_addr, clnt_addr;
    // define the socket size for client separately in a different memory to handle changing client sockets
    socklen_t clnt_adr_sz;

    if(argc != 2)
    {
        printf("Usage: %s <IP> <port>", argv[0]);
        exit(1);
    }

    // PF_INET, PF -> protocol family (PF_INET = AF_INET)
    // AF_INET, AF -> Address family 
    serv_sock = socket(PF_INET, SOCK_STREAM, 0);
    if(serv_sock == -1)
        error_handling("socket() error!");

    // initializes serv_addr to 0 -> to initialize sin_zero member to zero for conformity with struct sockaddr
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(atoi(argv[1]));

    if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1)
        error_handling("bind() error");

    if(listen(serv_sock, 5) == -1)
        error_handling("listen() error");

    clnt_adr_sz = sizeof(clnt_addr);

    while(1)
    {
        clnt_sock = accept(serv_sock, (struct sockaddr*) &clnt_addr, &clnt_adr_sz);
        if(clnt_sock == -1)
            error_handling("accept() error");
        else
            printf("Connected to client %d \n", i);

        while((str_len = read(clnt_sock, message, BUF_SIZE)) != 0)
        {
            write(clnt_sock, message, str_len);
        }

        close(clnt_sock);
    }
    close(serv_sock);
    return 0;
}

void error_handling(char *message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}

