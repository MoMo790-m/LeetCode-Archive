class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            rightsum = sum(nums[:i + 1])
            leftsum = sum(nums[i:])
            if rightsum == leftsum:
                return i
        return -1
        