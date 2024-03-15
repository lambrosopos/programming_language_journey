#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 32

int split_string(char line[]) {
  char *token=strtok(line, "-");
  token=strtok(NULL, "-");

  return atoi(token);
}

int main(int argc, char *argv[]) {
  int N;
  char line[BUF_SIZE];
  int count=0;

  scanf("%d", &N);

  while(N--){
    scanf("%s", line);

    if(split_string(line) <= 90) {
      count++;
    }
  }

  printf("%d\n", count);

  return 0;
}
