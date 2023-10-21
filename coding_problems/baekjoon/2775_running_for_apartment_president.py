total_len = int(input())

apartment_limit = 15

apartment = [[0] * apartment_limit for _ in range(apartment_limit)]

for i in range(apartment_limit):
    for j in range(apartment_limit):
        if i == 0:
            apartment[i][j] = j + 1
        elif j == 0:
            apartment[i][j] = 1
        else:
            apartment[i][j] = apartment[i - 1][j] + apartment[i][j - 1]


for i in range(total_len):
    floor = int(input())
    room = int(input())

    print(apartment[floor][room - 1])
