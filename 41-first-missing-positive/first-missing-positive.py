class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        len_nums = len(nums)

        for num in range(1,len_nums + 2):
            if num not in num_set:
                return num