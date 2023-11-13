import sys

N, M = map(int, sys.stdin.readline().split())

invisible = {}

for _ in range(N):
    name = sys.stdin.readline().strip()
    invisible[name] = 1

for _ in range(M):
    name = sys.stdin.readline().strip()
    if invisible.get(name) is None:
        invisible[name] = 1
    else:
        invisible[name] += 1

noone = []
for key, val in invisible.items():
    if val > 1:
        noone.append(key)

noone.sort()

print(len(noone))
print(*noone, sep="\n")
