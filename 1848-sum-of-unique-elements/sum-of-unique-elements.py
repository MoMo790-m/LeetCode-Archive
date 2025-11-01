class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        res = {}
        sum = 0

        for num in nums:
            res[num] = 1 + res.get(num,0)

        for key,val in res.items():
            if val == 1:
                sum+=key
        
        return sum
        