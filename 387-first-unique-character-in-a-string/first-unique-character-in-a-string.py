class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_chr = {}

        for word in s:
            freq_chr[word] = freq_chr.get(word,0) + 1
        
        for key in freq_chr:
            if freq_chr[key] == 1:
                return s.find(key)
        return -1 