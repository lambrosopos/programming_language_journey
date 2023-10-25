height, width = map(int, input().split())

board = [""] * height
for i in range(height):
    board[i] = input()


def get_count(h_idx, w_idx):
    count = 0
    color = ("W", "B")
    flag = 0
    for i in range(8):
        for j in range(8):
            painted = board[h_idx + i][w_idx + j] 
            if painted != color[flag]:
                # print(f"{painted=}, {color[flag]}")
                count += 1

            flag = (flag + 1) % 2
        flag = (flag + 1) % 2


    return min(count, 64 - count)

    

min_count = height * width
for i in range(height - 7):
    for j in range(width - 7):
        count = get_count(i, j)
        min_count = min(count, min_count)



print(min_count)
