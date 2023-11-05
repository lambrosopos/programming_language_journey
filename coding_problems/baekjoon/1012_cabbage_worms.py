import sys
sys.setrecursionlimit(10000)

def mark_searched(x: int, y: int, farm: list[list[int]]):
    """
    Check if NESW are 1. If so, change to -1

    Directions order: N, E, S, W

    North -> Negative Y
    East  -> Positive X
    South -> Positive Y
    West  -> Negative X
    """
    # Mark current position as explored
    farm[y][x] = -1

    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

    width, height = len(farm[0]), len(farm)

    for delta_x, delta_y in directions:
        if 0 <= x + delta_x < width and 0 <= y + delta_y < height:
            if farm[y + delta_y][x + delta_x] == 1:
                # Continue search if delta square is also a 1
                mark_searched(x + delta_x, y + delta_y, farm)


def solve(width: int, height: int, cabbages: int):
    """
    Solves a problem for cabbage worms. Also responsible for reading stdin for total of cabbages.
    """

    # Create a 2D matrix for width and height and fill with zero.
    farm = [[0] * width for _ in range(height)]

    # Fill cabbages with 1
    for _ in range(cabbages):
        coord_x, coord_y = map(int, sys.stdin.readline().split())
        farm[coord_y][coord_x] = 1


    # Loop around the farm and if 1, start go until the area is searched.
    # Increase count += 1
    count = 0
    for y in range(height):
        for x in range(width):
            if farm[y][x] == 1:
                mark_searched(x, y, farm)
                count += 1

    return count


def main(total_questions: int):
    answers = []
    for _ in range(total_questions):
        width, height, cabbages = map(int, sys.stdin.readline().split())
        answers.append(solve(width, height, cabbages))

    for a in answers:
        print(a)

if __name__ == "__main__":
    total_questions = int(sys.stdin.readline())
    main(total_questions)
