import sys

N, start_time = map(int, sys.stdin.readline().split())

min_wait = []
for _ in range(N):
    start, interval, bus_N = map(int, sys.stdin.readline().split())

    for i in range(bus_N):
        bus_time = start + interval * i

        if bus_time >= start_time:
            min_wait.append(bus_time - start_time)

if len(min_wait) == 0:
    print(-1)
else:
    print(min(min_wait))
