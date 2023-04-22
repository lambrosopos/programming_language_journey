#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#define BUF_SIZE 100

void error_handling(char* message);

int main(int argc, char* argv[])
{
    int fd1, fd2;
    char buf[BUF_SIZE];

    if(argc!=3)
        printf("Usage : %s <source_filepath> <dest_filepath>", argv[0]);

    fd1 = open(argv[1], O_RDONLY);
    if(fd1==-1)
        error_handling("open() error!");

    if(read(fd1, buf, sizeof(buf))==-1)
        error_handling("read() error!");

    printf("%s", buf);

    fd2 = open(argv[2], O_CREAT|O_WRONLY|O_TRUNC);
    if(fd2==-1)
        error_handling("open() error!");

    if(write(fd2, buf, sizeof(buf))==-1)
        error_handling("write() error");

    close(fd1); close(fd2);
    return 0;
}

void error_handling(char* message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}