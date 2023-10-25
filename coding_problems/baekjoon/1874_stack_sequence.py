import sys

total_len = int(sys.stdin.readline().strip())
num_list = [0] * total_len
for i in range(total_len):
    num_list[i] = int(input())

stack = []
ans = ""
idx = 0
cur_num = 1
while idx < total_len and cur_num < total_len + 2:
    # print(f"{idx=}, {cur_num=}, {ans=}, {stack=}, {num_list=}")
    num = num_list[idx]
    if len(stack) > 0 and stack[-1] == num:
        stack.pop()
        ans += "-"
        idx += 1
    else:
        stack.append(cur_num)
        cur_num += 1
        ans += "+"

if idx < total_len - 1:
    print("NO")
else:
    for c in ans:
        print(c)





