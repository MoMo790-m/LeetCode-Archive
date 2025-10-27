from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_ana = defaultdict(list)
        res = []

        for word in strs:
            sorted_word = tuple(sorted(word))
            group_ana[sorted_word].append(word)
        for val in group_ana.values():
            res.append(val)
        return res


        