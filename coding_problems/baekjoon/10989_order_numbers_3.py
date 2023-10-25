import sys

N  = int(sys.stdin.readline())
arr = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001): 
    if arr[i] != 0:
    	print(f"{i}\n" * arr[i], end="")
