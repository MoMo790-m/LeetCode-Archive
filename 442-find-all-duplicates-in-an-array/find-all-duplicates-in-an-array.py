class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for key, val in count.items():
            if val > 1:
                res.append(key)
        
        return res
        