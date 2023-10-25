import sys

total_len = int(sys.stdin.readline())

difficulties = [0] * total_len
for i in range(total_len):
    difficulties[i] = int(sys.stdin.readline())

difficulties.sort()
# print(difficulties)

extreme_count = round(total_len * 0.15)

if total_len <= 0:
    print(0)
else:
    difficulty_filtered = difficulties[extreme_count:total_len - extreme_count]
    difficulty_avg = sum(difficulty_filtered) / len(difficulty_filtered)

    print(round(difficulty_avg))



