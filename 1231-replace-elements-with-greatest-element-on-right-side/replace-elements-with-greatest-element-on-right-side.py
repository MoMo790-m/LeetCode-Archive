class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        siffix = [None] * n
        curr = -1

        for i in range(n - 1,-1,-1):
            siffix[i] = curr
            curr = max(curr,arr[i])
        return siffix
        