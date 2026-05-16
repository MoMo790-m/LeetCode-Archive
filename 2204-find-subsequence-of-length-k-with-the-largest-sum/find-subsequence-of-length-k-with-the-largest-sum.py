class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        top_k = sorted(nums, reverse=True)[:k]

        res = []

        for num in nums:
            if num in top_k:
                res.append(num)
                top_k.remove(num)

        return res