# Start 14:10
import sys

N, M = map(int, sys.stdin.readline().split())
products = list(map(int, sys.stdin.readline().split()))
requests = list(map(int, sys.stdin.readline().split()))

products.sort()

def find(num: int) -> str:
    """
    if exists => yes
          not => no
    """
    left = 0
    right = len(products) - 1

    while left <= right:
        mid = (left + right) // 2

        if products[mid] == num:
            return "yes"
        elif products[mid] > num:
            right = mid - 1
        elif products[mid] < num:
            left = mid + 1

    return "no"


ans = []
for r in requests:
    ans.append(find(r))

for a in ans:
    print(a)
