import sys
import time

start = time.time()

N = int(sys.stdin.readline())

total = 0
nums = [0] * 4474
idx = 1
break_next = False
while True:
    nums[idx] = total + idx
    total += idx
    idx += 1

    if break_next:
        break

    if total >= 10_000_000:
        break_next = True

ans = ""
for i, num in enumerate(nums):
    if N <= num:
        start_num = nums[i - 1] + 1
        delta_num = N - start_num
        if i % 2 == 1:
            # start from left
            ans += f"{i - delta_num}/{delta_num + 1}"
        else:
            # start from right
            ans += f"{delta_num + 1}/{i - delta_num}"

        break

print(ans)
