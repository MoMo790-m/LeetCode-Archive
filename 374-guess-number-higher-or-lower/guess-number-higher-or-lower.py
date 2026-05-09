

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1 , n

        while l <=r:
            m = (l + r) //2

            num = guess(m)

            if num == -1:
                r = m - 1
            elif num == 1:
                l = m + 1
            else:
                return m
        