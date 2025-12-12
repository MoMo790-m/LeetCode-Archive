class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)**2

        freq = {}
        res = []
        for row in grid:
            for num in row:
                freq[num] = 1 + freq.get(num,0)
                if freq[num] > 1:
                    res.append(num)
        
        seen = set(freq.keys())
        for i in range(1, n + 1):
            if i not in seen:
                res.append(i)
        
        return res

        