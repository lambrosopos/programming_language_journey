import sys

N, M = map(int, sys.stdin.readline().split())

"""
print 1 for M times.
print 2 for M - 1 times.
print 3 for M - 2 times.
"""

def print_recur(start, end, count):
    for i in range(start, end + 1
