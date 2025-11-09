from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:          
            return False

        seen = {}  
        for i, num in enumerate(nums):
            if num in seen:
                
                if i - seen[num] <= k:
                    return True
            
            seen[num] = i
        return False

        