class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      res=[]
      c=0
      maxl=max(len(word1),len(word2))
      while c<maxl:
        if c<len(word1):
            res.append(word1[c])
        if c<len(word2):
            res.append(word2[c])
        c+=1
      return "".join(res)
      