import sys

N = int(sys.stdin.readline())

board = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

def dnc(coord: tuple[int, int], len_n: int) -> tuple[int, int]:
    """
    Receives the starting upper left coordinates and the length it should search for

    Coordinates is a tuple of i and j, where i is height (y) and j is width (x)

    Returns:
         - tuple of two integers, blue and white respectively (blue = 1, white = 0)
    """
    first_val = board[coord[0]][coord[1]]

    # Check if all the values of given board is the same
    is_same = True
    for i in range(coord[0], coord[0] + len_n):
        for j in range(coord[1], coord[1] + len_n):
            if board[i][j] != first_val:
                is_same = False
                break

    if is_same:
        return (0, 1) if first_val == 0 else (1, 0)

    # If not the same, split board into four, and repeat process
    new_len = len_n // 2

    b, w = 0, 0

    b1, w1 = dnc((coord[0], coord[1] + new_len), new_len) # Quadrant I
    b2, w2 = dnc(coord, new_len) # Quadrant II
    b3, w3 = dnc((coord[0] + new_len, coord[1]), new_len) # Quadrant III
    b4, w4 = dnc((coord[0] + new_len, coord[1] + new_len), new_len) # Quadrant IV

    b += b1 + b2 + b3 + b4
    w += w1 + w2 + w3 + w4

    return (b, w)

b, w= dnc((0, 0), N)

print(w)
print(b)

