import sys

N = int(sys.stdin.readline())
words = [int(_) for _ in sys.stdin.readline().split()]

count_dict = {}
for i in words:
    if count_dict.get(i):
        count_dict[i] += 1
    else:
        count_dict[i] = 1

highest = 0
is_contradict = False
for key, val in count_dict.items():
    if key == 0 and val >= 1:
        is_contradict = True

    if key == val and key > highest:
        highest = key

if highest == 0 and is_contradict:
    print(-1)
else:
    print(highest)
