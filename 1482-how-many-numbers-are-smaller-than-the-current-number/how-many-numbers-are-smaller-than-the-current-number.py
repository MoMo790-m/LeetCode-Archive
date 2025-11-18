class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        post = {}

        for i , num in enumerate(sorted_nums):
            if num not in post:
                post[num] = i
            
        res = [post[num] for num in nums]
        return res


        