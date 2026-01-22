class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = x 
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        
        return rev == orig

