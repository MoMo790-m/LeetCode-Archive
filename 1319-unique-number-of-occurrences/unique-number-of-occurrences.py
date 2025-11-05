class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for i in arr:
            freq[i] = 1 + freq.get(i,0)

        val = list(freq.values())
        unique_val = set(val)

        return len(val) == len(unique_val)
        