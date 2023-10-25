number = int(input())

def factorial(result, num):
    if num <= 0:
        return result
    
    return factorial(result * num, num - 1)

final_num = factorial(number, number - 1)
num_str = str(final_num)

count = 0
for i in range(len(num_str) - 1, -1, -1):
    if num_str[i] != "0":
        break

    count += 1

if number == 0:
    print(0)
else:
    print(count)



