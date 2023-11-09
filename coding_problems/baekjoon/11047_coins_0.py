import sys
num_coins, amount = map(int, sys.stdin.readline().split())

coins = [0] * num_coins
for i in range(num_coins):
    coins[i] = int(sys.stdin.readline())


count = 0
for i in range(num_coins - 1, -1, -1):
    if amount == 0:
        break

    div_count = amount // coins[i]
    if div_count > 0:
        amount -= div_count * coins[i]
        count += div_count
    
print(count)

