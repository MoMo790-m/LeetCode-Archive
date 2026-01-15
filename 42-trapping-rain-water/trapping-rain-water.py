class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0 , len(height) - 1
        max_left,max_right = 0,0
        area = 0

        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left,height[left])
                water = max_left - height[left]
                area+=water
                left+=1
            else:
                max_right = max(max_right,height[right])
                water = max_right - height[right]
                water = max_right - height[right]
                area+=water
                right-=1

        return area 
        