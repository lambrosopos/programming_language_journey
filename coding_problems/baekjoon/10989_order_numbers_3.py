total_len = int(input())

num_list = [0] * total_len
for i in range(total_len):
    num_list[i] = int(input())

num_list.sort()

for n in num_list:
    print(n)
