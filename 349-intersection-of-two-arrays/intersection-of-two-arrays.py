class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        res = []

        for num in nums1:
            if num in nums2:
                s.add(num)
        for i in s:
            res.append(i)
        
        return res
        