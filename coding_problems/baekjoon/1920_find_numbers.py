import sys

target_len = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))
source_len = int(sys.stdin.readline())
source_list = list(map(int, sys.stdin.readline().split()))

num_map = {}

for num in target_list:
    num_map[num] = True

for num in source_list:
    print(int(num_map.get(num, False)))
