import sys

N = int(sys.stdin.readline())

s = set()

for _ in range(N):
    commands = sys.stdin.readline().split()

    c = commands[0]

    if c == "add":
        s.add(commands[1])
    elif c == "remove":
        s.discard(commands[1])
    elif c == "check":
        if commands[1] in s:
            print(1)
        else:
            print(0)
    elif c == "toggle":
        if commands[1] in s:
            s.discard(commands[1])
        else:
            s.add(commands[1])
    elif c == "all":
        for i in range(1, 21):
            s.add(str(i))
    elif c == "empty":
        s = set()
