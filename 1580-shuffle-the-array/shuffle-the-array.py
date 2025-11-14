class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n]
        right = nums[n:]

        res = []

        for i in range(n):
            res.append(left[i])
            res.append(right[i])
        
        return res
        