class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        all_words = list(zip(strs[0], strs[1], strs[2]))
        for x in all_words:
            if x[0] == x[1] == x[2]:
                res = res + str(x[0])
        return res