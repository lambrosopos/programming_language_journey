target_num = int(input())

count = 1
max_num = 1
while max_num < target_num:
    max_num += count * 6
    count += 1

print(count)
