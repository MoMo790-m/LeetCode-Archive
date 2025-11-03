class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        res = sum(ord(ch) for ch in t) - sum(ord(ch) for ch in s)

        return chr(res)

        