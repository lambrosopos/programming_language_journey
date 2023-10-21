total_len = int(input())

def ox_quiz(ox_string: str):
    total = 0
    sum = 0
    for c in ox_string:
        if c == "O":
            sum += 1
            total += sum
        else:
            sum = 0
            
    return total

for i in range(total_len):
    ox_string = input()
    print(ox_quiz(ox_string))
