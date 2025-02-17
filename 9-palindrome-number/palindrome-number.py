class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_list = []
        if x < 0 :
            return False
        while x > 0 :
            digit = x % 10
            number_list.insert(0,digit)
            x //=10
        return number_list == number_list[::-1] 

