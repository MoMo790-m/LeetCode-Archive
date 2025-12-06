class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = 0
        
        while l < len(flowerbed):
            if flowerbed[l] == 1:
                l+=1
                continue

            prev = 0 if l == 0 else flowerbed[l - 1]
            next_ = 0 if l == len(flowerbed) - 1 else flowerbed[l + 1]

            if flowerbed[l] == 0 and prev == 0 and next_ == 0:
                n-=1
                flowerbed[l] = 1

            l+=1
        
        return n <= 0
        