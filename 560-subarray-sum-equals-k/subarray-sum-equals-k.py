class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Csum = res = 0
        prefix = {0:1}

        for num in nums:
            Csum+=num
            diff= Csum - k

            res+=prefix.get(diff,0)
            prefix[Csum] = 1 + prefix.get(Csum,0)
        
        return res