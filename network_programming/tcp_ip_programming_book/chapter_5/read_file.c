#include <stdio.h>
#include <stdlib.h>

#define BUF_SIZE 1024

int main(int argc, char *argv[]) {
  char line[BUF_SIZE];
  FILE *f_ptr;

  f_ptr=fopen("example.txt", "rt");

  if(f_ptr == NULL) {
    printf("Failed to open file\n");
    exit(1);
  }

  while(fgets(line, BUF_SIZE, f_ptr) != NULL) {
    printf("%s", line);
  }

  fclose(f_ptr);
  return 0;
}
