def check_distance(start_num, end_num):
    if start_num % 3 == 2:
        # already in middle line
        return abs(end_num - start_num)
    elif start_num % 3 == 1:
        return abs(start_num + 1 - end_num)
    else:
        return abs(start_num - 1 - end_num)


def solution(numbers, hand):
    answer = ""

    left_pos, right_pos = (10, 12)
    for i, n in enumerate(numbers):
        if n == 0:
            n = 11

        position = n % 3

        if position == 1:
            answer += "L"
            left_pos = n
        elif position == 0:
            answer += "R"
            right_pos = n
        else:
            left_distance = check_distance(left_pos, n)
            right_distance = check_distance(right_pos, n)

            if left_distance < right_distance:
                answer += "L"
                left_pos = n
            elif left_distance > right_distance:
                answer += "R"
                right_pos = n
            else:
                if hand == "right":
                    answer += "R"
                    right_pos = n
                else:
                    answer += "L"
                    left_pos = n

    return answer

if __name__ == "__main__":
    ans = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
    print(ans)
