class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        perfect_sum = n * ( n + 1) // 2
        real_sum = sum(nums)
        
        unique_num = set(nums)
        unique_num_sum = sum(unique_num)
        
        duplicate_num = real_sum - unique_num_sum
        missing_num = perfect_sum - unique_num_sum
        
        res.append(duplicate_num)
        res.append(missing_num)
        
        return res
        