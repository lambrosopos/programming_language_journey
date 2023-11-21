import sys

N = int(sys.stdin.readline())

buildings = list(map(int, sys.stdin.readline().split()))

def find_c(idx: int, m: float):
    return buildings[idx] - (m * idx)

def find_m(from_idx: int, to_idx: int):
    delta_x = from_idx - to_idx
    delta_y = buildings[from_idx] - buildings[to_idx]

    return delta_y / delta_x

def is_higher(idx: int, m: float, c: float):
    left_side = buildings[idx]
    right_side = (m * idx) + c

    if left_side > right_side:
        return True
    else:
        return False

def solve(start_idx: int):
    # Right buildings
    right_idx = start_idx + 1

    max_right = 0
    while right_idx < N:
        m = find_m(start_idx, right_idx)
        c = find_c(start_idx, m)

        print(f"{start_idx=}, {right_idx=}, {max_right=}")

        if not is_higher(right_idx, m, c):
            max_right += 1

        right_idx += 1

    # Left buildings
    # left_idx = start_idx - 1
    # max_left = 0
    # while left_idx > 0:
    #     m = find_m(start_idx, left_idx)
    #     c = find_c(start_idx, m)

    #     count = 0
    #     for i in range(left_idx, start_idx):
    #         if is_higher(i, m, c):
    #             break

    #         count += 1

    #     max_left = max(max_left, count)
    #     left_idx -= 1

    # print(f"{start_idx=}, {max_left=}, {max_right=}")
    
    return max_right
    return max_right + max_left

# max_buildings = 0
# for i in range(N):
#     max_buildings = max(max_buildings, solve(i))
max_buildings = solve(4)

print(f"{max_buildings=}")
