import sys

n, nth_num = map(int, sys.stdin.readline().split())

ans = []
queue_list = list(range(1, n + 1))
count = 1
while len(queue_list) > 0:
    cur_num = queue_list.pop(0)
    
    if count % nth_num == 0:
        ans.append(str(cur_num))
    else:
        queue_list.append(cur_num)

    count += 1

ans = ", ".join(ans)

print(f"<{ans}>")
