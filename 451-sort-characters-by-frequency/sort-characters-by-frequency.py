class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for i in s:
            freq[i] = 1 + freq.get(i,0)
        
        l = []
        for key,val in freq.items():
            l.append([key,val])
        
        l = sorted(l,key=lambda x: x[1], reverse=True)
        
        res = '' 
        for char,count in l:
            res += char * count
        
        return res