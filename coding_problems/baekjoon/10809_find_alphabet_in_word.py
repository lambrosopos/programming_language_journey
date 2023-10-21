alphabets = "abcdefghijklmnopqrstuvwxyz"

word = input()

ans = [-1] * len(alphabets)
for i, a in enumerate(alphabets):
    for j, c in enumerate(word):
        if a == c:
            ans[i] = j
            break

print(" ".join([str(_) for _ in ans]))
