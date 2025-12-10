from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        min_chr = None 
        max_chr = 0

        for key,val in freq.items():
            if val % 2 != 0:
                max_chr = max(max_chr,val)
            else:
                if min_chr is None or val < min_chr:
                    min_chr = val
        
        return max_chr - min_chr