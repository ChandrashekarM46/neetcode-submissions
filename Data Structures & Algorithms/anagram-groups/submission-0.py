class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     group={}
     for s in strs:
        sort="".join(sorted(s))

        if sort not in group:
            group[sort]=[]
        group[sort].append(s)

     return list(group.values())
