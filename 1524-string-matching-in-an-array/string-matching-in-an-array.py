class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sol = []

        for i in range(len(words)):
            for j in range(len(words)):
                if j != i and words[i] in words[j]:
                    sol.append(words[i])
                    break

        return sol      