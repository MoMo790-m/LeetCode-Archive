class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return nums1
        
        for i in range(n):
            nums1[i + m] = nums2[i]

        l,r = 0, len(nums1) - 1

        while l < r:
            if nums1[l] > nums1[l+1]:
                nums1[l] ,nums1[l + 1] = nums1[l+1] , nums1[l]
            l+=1

            if l >= r:
                l = 0
                r-=1
        
        return nums1

        