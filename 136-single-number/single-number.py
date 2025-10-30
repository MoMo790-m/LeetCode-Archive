class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}

        for num in nums:
            res[num] = 1 + res.get(num,0)
        
        for key, val in res.items():
            if val == 1:
                return key


        
        