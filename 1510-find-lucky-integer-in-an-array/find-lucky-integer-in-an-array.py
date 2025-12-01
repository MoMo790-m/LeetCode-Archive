class Solution:
    def findLucky(self, arr: List[int]) -> int:

        return max((x for x in set(arr) if arr.count(x) == x), default = -1)
        