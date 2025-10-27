class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for num in nums:
            if num not in result:
                result.add(num)
            elif num in result:
                return True
        return False
        

        