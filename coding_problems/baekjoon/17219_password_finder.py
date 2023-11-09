import sys

n_pass, n_search = map(int, sys.stdin.readline().split())

pass_dict = {}
for _ in range(n_pass):
    site, password = sys.stdin.readline().split()
    pass_dict[site] = password

answers = [""] * n_search
for i in range(n_search):
    site = sys.stdin.readline().strip()
    answers[i] = pass_dict[site]

for a in answers:
    print(a)
