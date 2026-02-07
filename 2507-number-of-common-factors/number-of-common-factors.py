class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        min_val = min(a,b)
        res = 0

        for n in range(1,min_val + 1):
            if a % n == 0 and b % n == 0:
                res+=1
        
        return res
        