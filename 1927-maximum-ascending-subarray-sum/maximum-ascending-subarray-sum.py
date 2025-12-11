class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        count = nums[0]
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += nums[i + 1]  
            else:
                count = nums[i + 1]  
                
            res = max(res, count)
        
        return res
