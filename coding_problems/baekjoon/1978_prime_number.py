total_len = int(input())
numbers = list(map(int, input().split()))

count = 0
for n in numbers:
    if n == 1:
        continue

    skip_flag = False
    for i in range(2, n):
        if skip_flag:
            break

        if not skip_flag and n % i == 0:
            skip_flag = True

    if not skip_flag:
        count += 1

print(count)
