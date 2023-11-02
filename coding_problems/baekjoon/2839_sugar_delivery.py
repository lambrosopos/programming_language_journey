import sys

sugar = int(sys.stdin.readline())

bags = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bags += sugar // 5
        break
    
    sugar -= 3
    bags += 1

print(-1 if sugar < 0 else bags)
