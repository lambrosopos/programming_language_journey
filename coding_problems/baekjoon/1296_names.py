import sys

main_name = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

LOVE_WORD = "LOVE"

def init_count():
    love_dict = {}
    for c in LOVE_WORD:
        love_dict[c] = 0

    for c in main_name:
        if love_dict.get(c) == 0:
            love_dict[c] += 1

    return love_dict

def score(name: str):
    love_dict = init_count()

    for c in name:
        if love_dict.get(c):
            love_dict[c] += 1

    total = 1

    for i in range(4):
        for j in range(i + 1, 4):
            total *= (love_dict[LOVE_WORD[i]] + love_dict[LOVE_WORD[j]])

    return total % 100


scores = []
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    scores.append([name, score(name)])

scores.sort(key=lambda _: (-_[1], _[0]))

print(scores[0][1])
