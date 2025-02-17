class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(log n) 
        l = 0 
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2   
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1  
            else:
                r = mid - 1

        return l


 




"""
 o(n logn) 
         for i in range(len(nums)) :
            if  nums[i] ==  target:
                return i
                
        nums.append(target)
        nums.sort()
        return nums.index(target)
"""
    
        