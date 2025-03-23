class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1 
        digits = list(map(int,str(num)))
        return digits
        