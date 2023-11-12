import sys

numbers = list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcd(a, b):
    return (a * b) // gcd(a, b)

least_num = None
for i in range(5):
    for j in range(5):
        if i == j:
            continue
        for k in range(5):
            if j == k or i == k:
                continue
            smallest_num = lcd(numbers[i], lcd(numbers[j], numbers[k]))

            if least_num is None:
                least_num = smallest_num
            else:
                least_num = min(least_num, smallest_num)

print(least_num)

