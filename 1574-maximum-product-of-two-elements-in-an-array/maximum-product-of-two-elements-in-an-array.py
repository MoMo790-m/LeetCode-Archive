class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        a = -heapq.heappop(nums)
        b = -heapq.heappop(nums)

        return (a - 1) * (b - 1)

        