#include <stdio.h>
#include <time.h>

#define BUF_SIZE 3
// #define BUF_SIZE 4096

int main(int argc, char *argv[]) {
  clock_t start = clock();

  FILE *fp1;
  FILE *fp2;

  char buf[BUF_SIZE];

  fp1=fopen("news.txt", "r");
  fp2=fopen("cpy_stdcpy.txt", "w");

  while(fgets(buf, BUF_SIZE, fp1) != NULL) {
    fputs(buf, fp2);
  }

  fclose(fp1);
  fclose(fp2);

  clock_t end=clock();
  float seconds=(float)(end-start)/CLOCKS_PER_SEC;

  printf("%f", seconds);

  return 0;
}
