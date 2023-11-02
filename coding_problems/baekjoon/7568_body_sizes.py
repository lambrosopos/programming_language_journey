import sys

total_len = int(sys.stdin.readline())

body_sizes = []
for _ in range(total_len):
    body_sizes.append(list(map(int, sys.stdin.readline().split())))

body_ranks = [1] * total_len

for idx, s in enumerate(body_sizes):
    for s_2 in body_sizes:
        if s == s_2:
            continue

        if s[0] < s_2[0] and s[1] < s_2[1]:
            body_ranks[idx] += 1

print(" ".join([str(_) for _ in body_ranks]))

