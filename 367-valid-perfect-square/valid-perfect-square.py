class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqRoot = int((num)**.5)
        return sqRoot * sqRoot == num
        