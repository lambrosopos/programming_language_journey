def print_palindrome(num: str):
    left_ptr = 0
    right_ptr = len(num) - 1

    while left_ptr < right_ptr:
        if num[left_ptr] != num[right_ptr]:
            return False

        left_ptr += 1
        right_ptr -= 1

    return True
    

while True:
    new_input = input()
    
    if new_input == "0":
        break
        
    ans = print_palindrome(new_input)
    print('yes' if ans else 'no')
