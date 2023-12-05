import sys

N = int(sys.stdin.readline())
points = []
for _ in range(N):
    points.append(list(map(int, sys.stdin.readline().split())))

points.sort()

# print(f"{points=}")


def solve():
    left = points[0][0]
    right = points[-1][0]

    while left <= right:
        mid = (left + right) // 2 

        # print(f"{mid=}")

        pairs_dict = {}
        for p in points:
            str_p = str(p)

            if p[0] == mid:
                continue

            if pairs_dict.get(str_p, 0) > 0:
                pairs_dict[str_p] -= 1
            else:
                reflect_distance = abs(mid - p[0]) * 2
                # if point is right of line
                if p[0] > mid:
                    x, y = p[0] - reflect_distance, p[1]
                    pairs_dict[str([x, y])] = 1
                else:
                    # Add the mid line
                    x, y = p[0] + reflect_distance, p[1]
                    pairs_dict[str([x, y])] = 1

            # print(f"{str_p=}, {pairs_dict=}")

        if sum(pairs_dict.values()) == 0:
            return mid

        if mid > left:
            left = mid + 1
        else:
            right = mid - 1

    if sum(pairs_dict.values()) == 0:
        return right
    else:
        return "NO"


print(solve())
