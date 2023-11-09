import sys

def parse_line(line: str):
    """
    Parses string to numbers and signs
    """
    parsed = []
    
    num = ""
    sign = "+"
    for c in line:
        if c == "+" or c == "-":
            parsed.append(int(sign + num))
            sign = c
            num = ""
        else:
            num += c 

    # add last number
    if len(num) > 0:
        parsed.append(int(sign+num))

    return parsed


def greedy(numbers: list[int]):
    num_sum = 0

    if len(numbers) == 0:
        return num_sum

    sign = 1

    for n in numbers:
        if n >= 0:
            num_sum += n * sign
        else:
            if sign == 1:
                sign = -1

            num_sum += n

    return num_sum





def main():
    line = sys.stdin.readline()
    parsed_numbers = parse_line(line)
    ans = greedy(parsed_numbers)

    print(ans)


if __name__ == "__main__":
    main()
