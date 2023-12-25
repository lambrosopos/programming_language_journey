import sys

N, M = map(int, sys.stdin.readline().split())

poke_dict = {}
for i in range(1, N + 1):
    name = sys.stdin.readline().rstrip()
    poke_dict[i] = name
    poke_dict[name] = i

answer = []
for i in range(1, M + 1):
    line = sys.stdin.readline().rstrip()
    try:
        line = int(line)
        answer.append(poke_dict[line])
    except:
        answer.append(poke_dict[line])

print(*answer, sep="\n")
