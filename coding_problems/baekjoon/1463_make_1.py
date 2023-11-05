import sys
sys.setrecursionlimit(10000)

target_num = int(sys.stdin.readline())

# Number 1 is 0 since there is nothing to do when number is 1
explored = {1:0}

def find_min(num: int):
    """
    Will recursively find number, until minimum number is found
    """
    if explored.get(num, None):
        return explored[num]

    if num % 3 == 0 and num % 2 == 0:
        explored[num] = min(find_min(num // 3), find_min(num // 2)) + 1
    elif num % 3 == 0:
        explored[num] = min(find_min(num // 3), find_min(num - 1)) + 1
    elif num % 2 == 0:
        explored[num] = min(find_min(num // 2), find_min(num - 1)) + 1
    else:
        explored[num] = find_min(num - 1) + 1


# Print the minimum number from explored dictionary
find_min(target_num)
print(explored[target_num])
