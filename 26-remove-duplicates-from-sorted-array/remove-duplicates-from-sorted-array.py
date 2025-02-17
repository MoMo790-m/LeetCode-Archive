class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq_num = 1
        for n in range(1,len(nums)):
            if nums[n] != nums[n -1]:
                nums[uniq_num] = nums[n]
                uniq_num +=1

        return uniq_num
        
