class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[temp_index] = nums[i]
                temp_index+= 1

        k = temp_index
        return k
        