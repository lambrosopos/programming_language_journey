import sys

H, W = map(int, sys.stdin.readline().split())

guards = [ sys.stdin.readline().strip() for _ in range(H) ]

h_guards = set()
v_guards = set()

for i in range(H):
    for j in range(W):
        if guards[i][j] == "X":
            h_guards.add(i)
            v_guards.add(j)

print(max(H - len(h_guards), W - len(v_guards)))
