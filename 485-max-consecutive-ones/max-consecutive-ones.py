class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count = 0
        max_cons = 0

        for num in nums:
            if num == 1:
                one_count +=1
                max_cons = max(max_cons,one_count)
            else:
                one_count = 0
        
        return max_cons
        