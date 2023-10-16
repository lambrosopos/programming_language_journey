class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        int_sum = 0
        
        for idx, val in enumerate(s):
            if idx != len(s) - 1 and val in ('I', 'X', 'C'):
                next_val = s[idx + 1]
                if val == 'I' and next_val in ('V', 'X'):
                    int_sum -= 1
                    continue
                elif val == 'X' and next_val in ('L', 'C'):
                    int_sum -= 10
                    continue
                elif val == 'C' and next_val in ('D', 'M'):
                    int_sum -= 100
                    continue
                    
            int_sum += roman_numerals[val]
                
        
        return int_sum
