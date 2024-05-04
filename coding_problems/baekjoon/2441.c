#include <stdio.h>

int main(int argc, char *argv[]) {
    int N;
    scanf("%d", &N);
    
    int i;
    int j;
    for(i=N; i>0; i--) {
        for(j=0; j<N-i; j++) {
            printf(" ");
        }
        for(j=0; j<i; j++) {
            printf("*");   
        }
        
        printf("\n");
    }
    
    return 0;
}
