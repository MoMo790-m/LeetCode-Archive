class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Two Pointer
        Single pass through both arrays: O(n + m)
        Total: O(n + m) -> more faster
        """
        
        i , j = 0,0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        
        res.extend(nums1[i:])
        res.extend(nums2[j:])

        return res

        
        
        """
        Hash Table approach -> 
        Building dictionaries: O(n + m)
        Creating union of sets: O(n + m)
        Sorting the keys: O(k log k) where k is the number of unique ids
        Building result: O(k)
        Total: O(n + m + k log k)

        dict1 = {}
        dict2 = {}

        for key,val in nums1:
            dict1[key] = val
        
        for key,val in nums2:
            dict2[key] = val
        
        return [[key , dict1.get(key,0) + dict2.get(key,0)] for key in sorted(set(dict1) | set(dict2))]

        """
        