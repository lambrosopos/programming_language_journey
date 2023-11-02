import sys

total_len = int(sys.stdin.readline())

coords = []
for _ in range(total_len):
    cX, cY = map(int, sys.stdin.readline().split())
    coords.append((cX, cY))
    
coords.sort(key=lambda _: (_[0], _[1]))

for c in coords:
    print(c[0], c[1])
