# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)[::-1]
        
        if x < 0:
            str_x = '-' + str_x[:-1]
            
        result = int(str_x)
        
        if result > 2147483648 or result < -2147483648:
            return 0
        
        return result 
