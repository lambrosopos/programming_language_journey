#include <stdio.h>
#include <string.h>

#define CHAR_SIZE 1000

int main(int argc, char *argv[]) {
  int N;
  char S[CHAR_SIZE];

  scanf("%d", &N);

  for(int i=0; i<N; i++) {
    char ABC[26]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int total=0;

    scanf("%s", S);

    for(int j=0; j<strlen(S); j++) {
      ABC[S[j]-65]=1;
    }

    for(int j=0; j<26; j++) {
      if(ABC[j] == 1) {
        total+=65+j;
      }
    }

    printf("%d\n", 2015-total);
  }
  
  return 0;
}
