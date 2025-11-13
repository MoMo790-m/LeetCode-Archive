class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0
        res = 0
        i = 0

        while i < len(s):
            if s[i] == '1':
                count_one += 1
            else:
                res += count_one
                while i + 1 < len(s) and s[i + 1] == '0':
                    i+=1
            i+=1
        
        return res
        