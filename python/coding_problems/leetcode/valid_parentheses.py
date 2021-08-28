class Solution:
    def isValid(self, s: str) -> bool:
        parens_dict = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif char in (')', ']', '}'):
                if len(stack) == 0 or stack[-1] != parens_dict.get(char):
                    return False
                stack.pop()
        
        if len(stack) != 0:
            return False
        
        return True
