import sys

num = sys.stdin.readline().strip()

ans = ""
for n in num:
    n = int(n)
    if 3 < n < 7:
        ans += "4"
    elif n == 0 or n >= 7:
        ans += "7"

print(int(ans))

