class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        strs.sort()
        j=0
        while j<len(strs[0]) and strs[0][j]==strs[-1][j]:
            j+=1
        return strs[0][:j]