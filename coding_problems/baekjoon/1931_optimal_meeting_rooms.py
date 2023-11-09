import sys

N = int(sys.stdin.readline())

hours = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    hours.append((start, end))

# Sort by ending hour
# hours.sort(key=lambda _: (_[1], _[0]))
hours.sort(key=lambda _: _[1])
print(hours)

count = 0
cur_hour = 0
for start, end in hours:
    if start >= cur_hour:
        cur_hour = end
        count += 1

print(count)
