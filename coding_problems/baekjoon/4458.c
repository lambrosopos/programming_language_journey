#include <ctype.h>
#include <stdio.h>

#define LINE_SIZE 31

void solve();

int main() {
  int N;
  scanf("%d", &N);
  getchar();

  char L[LINE_SIZE];
  for (int i = 0; i < N; i++) {
    scanf("%[^\n]%*c", L);

    L[0]=toupper(L[0]);

    printf("%s\n", L);
  }

  return 0;
}
