num_1, num_2, num_3 = int(input()), int(input()), int(input())

final_num = str(num_1 * num_2 * num_3)

digit_count = [0] * 10
for d in final_num:
    digit_count[int(d)] += 1

for d in digit_count:
    print(d)
