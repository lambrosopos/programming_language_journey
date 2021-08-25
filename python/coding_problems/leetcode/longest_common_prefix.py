class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        
        for idx, letter in enumerate(strs[0]):
            flag = True
            for word in strs[1:]:
                try:
                    if letter != word[idx]:
                        flag = False
                        break
                except:
                    flag = False
                    break
            if flag:
                result += letter
            else:
                break
                    
        return result
