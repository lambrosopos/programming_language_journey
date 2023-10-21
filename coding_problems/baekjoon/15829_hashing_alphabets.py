total_len = int(input())
word = input()

alpha = "abcdefghijklmnopqrstuvwxyz"

ans = 0

def get_alpha_value(character: str) -> int:
    for i, c in enumerate(alpha):
        if c == character:
            return i + 1

prime_number = 31
mod_number = 1234567891

for i, c in enumerate(word):
    a_val = get_alpha_value(c) 
    ans += a_val * (prime_number ** i)

print(ans % mod_number)
