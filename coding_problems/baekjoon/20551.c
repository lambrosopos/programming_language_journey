#include <stdio.h>
#include <stdlib.h>

int comp(const void *elem1, const void *elem2);
int binary_search(int nums[], int search_num, int L, int R);

int main(int argc, char *argv[]) {
  int i, N, M, S;

  scanf("%d %d", &N, &M);

  int nums[N];
  for(i=0; i<N; i++) {
    scanf("%d", &nums[i]);
  }

  qsort(nums, N, sizeof(int), comp);

  for(i=0; i<M; i++) {
    scanf("%d", &S);
    printf("%d\n", binary_search(nums, S, 0, N-1));
  }

  return 0;
}

int comp (const void * elem1, const void * elem2) 
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

int binary_search(int nums[], int search_num, int L, int R) {
  if(L > R) {
    return -1;
  }

  int mid=(L + R) / 2;

  if(nums[mid] == search_num) {
    return mid;
  } else if(nums[mid] > search_num) {
    return binary_search(nums, search_num, L, mid-1);
  } else {
    return binary_search(nums, search_num, mid+1, R);
  }
}
