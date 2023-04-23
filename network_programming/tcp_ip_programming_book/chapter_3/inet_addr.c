#include <stdio.h>
#include <arpa/inet.h>

unsigned long convert_inet(char *address)
{
    unsigned long conv_addr = inet_addr(address);
    if(conv_addr==INADDR_NONE)
        printf("Error occurred!");
    else
        printf("Network ordered integer addr: %#lx \n", conv_addr);

    return conv_addr;
}

int main(int argc, char *argv[])
{
    char *addr1 = "1.2.3.4";
    char *addr2 = "1.2.3.256";

    convert_inet(addr1);
    convert_inet(addr2);

    return 0;
}
