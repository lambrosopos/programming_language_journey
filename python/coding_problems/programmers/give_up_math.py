def solution(answers):
    # 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    # 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    # 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    pattern_1 = [1, 2, 3, 4, 5] #=> modulo 5
    pattern_2 = [1, 3, 4, 5] #=> if odd = 2 if even modulo 4
    pattern_3 = [3, 1, 2, 4, 5] #=> divide by 2 and round up

    person_1, person_2, person_3 = (0, 0, 0)

    for val, idx in enumerate(answers):
        if val == pattern_1[idx % 4]:
            person_1 += 1

        if idx % 2 == 0 and val == 2:
            person_2 += 1
        elif idx % 2 == 1 and val == pattern_2[idx % 3]:
            person_2 += 1

        if val == pattern_3[round(idx / 2)]:
            pattern_3 += 1

    return (person_1, person_2, person_3)


if __name__ == "__main__":
    problems = [1, 2, 3, 4, 5]
    ans = solution(problems)
    print(ans)
