class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        text1 = ''.join(word1)
        text2 = ''.join(word2)

        return text1 == text2