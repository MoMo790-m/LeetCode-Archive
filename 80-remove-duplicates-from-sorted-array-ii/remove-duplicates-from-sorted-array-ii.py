class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        count = 0
        prev = None 

        for num in nums:
            if num != prev:
                count = 1
                prev = num
            else:
                count+=1
            
            if count <= 2:
                nums[i] = num
                i+=1
        
        return len(nums[:i])