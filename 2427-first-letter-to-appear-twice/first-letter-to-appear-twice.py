class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = set()

        for chr in s:
            if chr in res:
                return chr
            else:
                res.add(chr)
        