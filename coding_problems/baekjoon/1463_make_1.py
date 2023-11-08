import sys

num = int(sys.stdin.readline())

s_dict = {1:0}
for i in range(2, num + 1):
    
    s_dict[i] = s_dict[i - 1] + 1

    if i % 3 == 0:
        s_dict[i] = min(s_dict[i], s_dict[i//3] + 1)

    if i % 2 == 0:
        s_dict[i] = min(s_dict[i], s_dict[i//2] + 1)

print(s_dict[num]
