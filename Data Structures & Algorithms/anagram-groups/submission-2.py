class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      mp={}
      for s in strs:
         a = "".join(sorted(s))
         if a not in mp:
            mp[a]=[]
         mp[a].append(s)
      return list(mp.values())
           