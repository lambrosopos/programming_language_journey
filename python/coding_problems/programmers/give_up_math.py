import math

def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5] #=> modulo 5
    pattern_2 = [1, 3, 4, 5] #=> if odd = 2 if even modulo 4
    pattern_3 = [3, 1, 2, 4, 5] #=> divide by 2 and round up

    persons = [0, 0, 0]

    for idx, val in enumerate(answers):
        if val == pattern_1[idx % 5]:
            persons[0] += 1

        if idx % 2 == 0 and val == 2:
            persons[1] += 1
        elif idx % 2 == 1 and val == pattern_2[idx % 4]:
            persons[1] += 1

        if val == pattern_3[math.floor(idx / 2)]:
            persons[2] += 1

    if persons[0] == persons[1] == persons[2]:
        return [1, 2, 3]
    
    highest_answer = persons[0]
    highest_person = []

    for idx, p in enumerate(persons):
        if p > highest_answer:
            highest_person = [idx + 1]
            highest_answer = p
        elif p == highest_answer:
            highest_person.append(idx + 1)

    return highest_person



if __name__ == "__main__":
    problems = [1, 2, 1, 2, 2]
    ans = solution(problems)
    print(ans)
