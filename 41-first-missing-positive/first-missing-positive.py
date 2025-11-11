class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        smallest = 1

        while smallest in num_set:
            smallest +=1

        return smallest        