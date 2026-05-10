class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r

        def canCap(cap):
            shipps , currCap = 1,cap
            for w in weights:
                if currCap - w <0:
                    shipps+=1
                    if shipps > days:
                        return False
                    currCap = cap
                
                currCap-= w
            return True

        while l<= r:
            cap = (l+r) // 2
            if canCap(cap):
                res = min(res,cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res
        