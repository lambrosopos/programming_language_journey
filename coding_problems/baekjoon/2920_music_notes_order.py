nums = [int(_) for _ in input().split()]

ans = 'ascending'

if nums[0] > nums[-1]:
    ans = 'descending'

for i, v in enumerate(nums):
    if i == 0 or ans == 'mixed':
        continue
    
    if v > nums[i - 1] and ans == 'descending':
        ans = 'mixed'
    elif v < nums[i - 1] and ans == 'ascending':
        ans = 'mixed'
    
print(ans)

