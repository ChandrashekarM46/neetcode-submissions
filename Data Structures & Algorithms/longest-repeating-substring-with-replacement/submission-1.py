class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      left=mfreq=length=maxl=0
      count={}

      for right in range(len(s)):
        count[s[right]]=count.get(s[right],0)+1
        mfreq=max(mfreq,count[s[right]])
        length= right - left + 1

        while length - mfreq > k:
            count[s[left]]-=1
            left+=1
            length=right-left+1
        
        maxl=max(maxl,length)
      return maxl
