import sys

submissions = [0 for _ in range(31)]

while True:
    line = sys.stdin.readline().rstrip()

    if line == "":
        break

    idx = int(line)
    submissions[idx] += 1

for i in range(1, 31):
    if submissions[i] == 0:
        print(i)
