import re

def main(new_id):
    new_id = new_id.lower()

    answer = ''
    
    for idx, char in enumerate(new_id):
        if re.match(r'[a-zA-Z0-9._-]', char):
            if char == '.':
                if (idx + 1) <= len(new_id) and new_id[idx + 1] == '.': 
                    continue
            answer += char

    if answer[0] == '.':
        answer = answer[1:]

    if answer == '':
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[:15]

    while len(answer) <= 2:
        answer += answer[-1]

    return answer


if __name__ == "__main__":
    answer = main("...!@BaT#*..y.abcdefghijklm")
    print(answer)
