import sys

num_len, num_problems = map(int, sys.stdin.readline().split())
numbers = [int(_) for _ in sys.stdin.readline().split()]

num_sum = [0] * (num_len + 1)
for i in range(1, num_len + 1):
    num_sum[i] = numbers[i - 1] + num_sum[i - 1]

answers = [0] * num_problems
for i in range(num_problems):
    start, end = map(int, sys.stdin.readline().split())
    answers[i] = num_sum[end] - num_sum[start - 1]

for a in answers:
    print(a)
