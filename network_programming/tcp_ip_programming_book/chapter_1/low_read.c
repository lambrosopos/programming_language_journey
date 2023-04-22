#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#define BUF_SIZE 100
void error_handling(char* message);

int main(int argc, char* argv[])
{
    int fd;
    char buf[BUF_SIZE];

    if(argc!=2)
    {
        printf("Usage: %s <filepath>\n", argv[0]);
        exit(1);
    }

    fd=open(argv[1], O_RDONLY);
    if(fd==-1)
        error_handling("open() error!");
    printf("file descriptor: %d \n", fd);

    if(read(fd, buf, sizeof(buf))==-1)
        error_handling("read() error!");
    printf("file data: %s", buf);

    close(fd);
    return 0;
}

void error_handling(char* message)
{
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}
