#include <string.h>
#include <stdio.h>

#define MAX_CHAR 256

int main(int argc, char *argv[]) {
  char name[MAX_CHAR];
  int age;
  int weight;

  while(1) {
    scanf("%s %d %d", name, &age, &weight);

    if(!strcmp(name, "#") && age==0 && weight==0) {
      break;
    }

    if(age > 17 || weight >= 80) {
      printf("%s Senior\n", name);
    } else {
      printf("%s Junior\n", name);
    }
  }

  return 0;
}
