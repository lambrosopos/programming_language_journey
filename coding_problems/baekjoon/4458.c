#include <stdio.h>
#include <ctype.h>

#define MAX_LINE_SIZE 31

int main() {
  int N;
  scanf("%d", &N);
  getchar(); // Consume newline character after reading N

  // Buffer to store each line
  char line[MAX_LINE_SIZE];

  for (int i = 0; i < N; i++) {
    fgets(line, MAX_LINE_SIZE, stdin);

    // Capitalize the first letter of the line
    if (isalpha(line[0])) {
      line[0] = toupper(line[0]);
    }

    // Output the modified line
    printf("%s", line);
  }

  return 0;
}
