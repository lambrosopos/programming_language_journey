total_len, target_num = map(int, input().split())
num_list = list(map(int, input().split()))

max_num = 0
for i in range(total_len):
    for j in range(i + 1, total_len):
        for k in range(j + 1, total_len):
            num_sum = num_list[i] + num_list[j] + num_list[k]

            if num_sum == target_num:
                max_num = num_sum
                break
            elif num_sum > max_num and num_sum < target_num:
                max_num = num_sum

print(max_num)
