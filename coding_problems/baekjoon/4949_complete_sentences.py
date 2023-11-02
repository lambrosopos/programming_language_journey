import sys

def is_stable(line: str) -> str:
    matching_parans = {
            "[": "]",
            "(": ")"
    }

    paran_stack = []
    for char in line:
        if char == "[" or char == "(":
            paran_stack.append(char)
        elif char == "]" or char == ")":
            if len(paran_stack) == 0:
                return "no"
            if matching_parans[paran_stack.pop()] != char:
                return "no"

    return "yes" if len(paran_stack) == 0 else "no"

ans = []
while True:
    line = sys.stdin.readline().replace("\n", "")

    if len(line) == 1 and line == ".":
        break
    
    ans.append(is_stable(line))

for a in ans:
    print(a)
