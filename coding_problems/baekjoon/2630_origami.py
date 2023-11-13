import sys
sys.setrecursionlimit(10_000)

N = int(sys.stdin.readline())

board = []
for _ in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    board.append(numbers)

BLUE, WHITE = 0, 0
def dnc(coords: tuple[int, int], board_len: int):
    global BLUE, WHITE

    start_color = board[coords[0]][coords[1]]
    all_same = True
    for i in range(coords[1], coords[0] + board_len):
        if all_same is False:
            break
        for j in range(coords[0], coords[1] + board_len):
            if all_same is False:
                break
            if board[i][j] != start_color:
                all_same = False

    print(f"{all_same=}, {coords=}, {BLUE=}, {WHITE=}, {board_len=}")
    
    if all_same:
        if start_color == 0:
            WHITE += 1 
        else: 
            BLUE += 1 
    else:
        half_len = board_len // 2 
        dnc(coords, half_len) 
        dnc((half_len, half_len), half_len)
        dnc((coords[0], half_len), half_len)
        dnc((half_len, coords[1]), half_len)



dnc((0, 0), N)

print(BLUE)
print(WHITE)
