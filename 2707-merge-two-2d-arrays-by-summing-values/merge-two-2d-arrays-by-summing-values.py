class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        dict2 = {}

        for key,val in nums1:
            dict1[key] = val
        
        for key,val in nums2:
            dict2[key] = val
        
        return [[key , dict1.get(key,0) + dict2.get(key,0)] for key in sorted(set(dict1) | set(dict2))]