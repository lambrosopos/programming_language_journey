nums = [None] * 9

for i in range(9):
    nums[i] = int(input())
    
max_num = nums[0]
max_idx = 1
for i, v in enumerate(nums):
    if v > max_num:
        max_num = v
        max_idx = i + 1

print(max_num)
print(max_idx)
