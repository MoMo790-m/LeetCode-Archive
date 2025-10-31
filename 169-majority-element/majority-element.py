class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        maj = n // 2

        res = {}

        for num in nums:
            res[num] = 1 + res.get(num,0)

        for key, val in res.items():
            if val > maj:
                return key
        