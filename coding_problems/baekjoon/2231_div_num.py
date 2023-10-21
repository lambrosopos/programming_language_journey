target_num = int(input())

min_num = 0
for num in range(target_num, -1, -1):
    div_num = num
    
    for c in str(num):
        div_num += int(c)
    
    if div_num == target_num:
        min_num = num

print(min_num)
