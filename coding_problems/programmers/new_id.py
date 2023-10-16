import re

def main(new_id):
    new_id = new_id.lower()

    answer = ''
    
    for idx, char in enumerate(new_id):
        if re.match(r'[a-zA-Z0-9._-]', char):
            if char == '.':
                try:
                    if new_id[idx + 1] == '.': 
                        continue
                except IndexError:
                    continue
            answer += char

    if answer[0] == '.':
        answer = answer[1:]


    if answer == '':
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[:15]

    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]

    while len(answer) <= 2:
        answer += answer[-1]

    return answer


if __name__ == "__main__":
    test_strings = [
        "...!@BaT#*..y.abcdefghijklm",
        "z-+.^.",
        "=.=",
        "123_.def",
        "abcdefghijklmn.p"
    ]

    for s in test_strings:
        answer = main(s)
        print(answer)
