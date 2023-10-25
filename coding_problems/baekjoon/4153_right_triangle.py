def check_right(width, length, hypo):
    if width ** 2 + length ** 2 == hypo ** 2:
        return "right"
    return "wrong"

while True:
    lines = list(map(int, input().split()))

    lines.sort()

    w, l, hypo = lines

    if w + l + hypo == 0:
        break

    ans = check_right(w, l, hypo)
    print(ans)

