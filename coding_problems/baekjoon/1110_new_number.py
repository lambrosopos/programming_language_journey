import sys

def main(start_num: str):
    nums_dict = {}
    num = start_num
    cycle = 1
    while True:
        if nums_dict.get(num):
            new_num = nums_dict[num]
        else:
            first_right = num[-1]

            if int(num) < 10:
                num = "0" + str(int(num))

            n_sum = 0
            for _ in num:
                n_sum += int(_)

            n_sum = str(n_sum)
            second_right = n_sum[-1]

            new_num = first_right + second_right

        if int(new_num) == int(start_num):
            break
        else:
            nums_dict[num] = new_num
            num = new_num

        cycle += 1

    return cycle

if __name__ == "__main__":
    start_num = sys.stdin.readline().strip()
    print(main(start_num))
