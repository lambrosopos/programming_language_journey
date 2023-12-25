import sys

num = sys.stdin.readline().rstrip()

is_ujinsoo = "NO"
for i in range(1, len(num)):
    first_num = 1
    for c in num[:i]:
        first_num *= int(c)

    second_num = 1
    for c in num[i:]:
        second_num *= int(c)

    if is_ujinsoo == "YES":
        break
    elif first_num == second_num:
        is_ujinsoo = "YES"

print(is_ujinsoo)
