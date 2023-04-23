#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <string.h>

int main(int argc, char *argv[])
{
    struct sockaddr_in addr; // decalre a socket address struct
    char *serv_ip = "211.217.168.12"; // declare a string value IP address
    char *serv_port="9190"; // declare a string value PORT address
    memset(&addr, 0, sizeof(addr)); // initialize addr members to value 0
    addr.sin_family = AF_INET; // assign address structure
    addr.sin_addr.s_addr = inet_addr(serv_ip); // initialize string value IP address -> create a byte array for network ordered bytes
    addr.sin_port = htons(atoi(serv_port)); // initialize string value port number -> create a network ordered bytes

    return 0;
}
