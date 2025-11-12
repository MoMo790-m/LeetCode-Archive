import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one_count = 0
        for num in nums:
            if num == 1:
                one_count += 1
        if one_count > 0:
            return len(nums) - one_count
        
        min_sub_len = float('inf')

        for l in range(len(nums)):
            cur_gcd = 0
            for r in range(l, len(nums)):
                if r - l >= min_sub_len:
                    break
                cur_gcd = math.gcd(cur_gcd,nums[r])
                if cur_gcd == 1:
                    min_sub_len = r - l + 1
                    break
        if min_sub_len == float('inf'):
            return -1
        return (min_sub_len - 1) + len(nums) - 1
