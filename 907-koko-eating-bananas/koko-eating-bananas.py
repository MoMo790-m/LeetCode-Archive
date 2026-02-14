class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1 , max(piles)

        res = r

        while l <= r:
            k = (l + r) // 2

            totaltime = 0
            for pile in piles:
                totaltime += math.ceil(float(pile) / k)
            if totaltime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
        