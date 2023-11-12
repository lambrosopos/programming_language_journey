import sys

N = int(sys.stdin.readline())

words = [ sys.stdin.readline() for _ in range(N) ]
word_len = len(words[0])

ans = ""
idx = 0
while idx < word_len:
    cur_char = words[0][idx]
    is_same = all([w[idx] == cur_char for w in words])

    ans += cur_char if is_same else "?"

    idx += 1

print(ans)

