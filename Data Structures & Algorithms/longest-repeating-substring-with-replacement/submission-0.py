class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       mp={}
       l=maxf=ans=0

       for r in range(len(s)):
        mp[s[r]]=mp.get(s[r],0)+1
        maxf=max(maxf,mp[s[r]])

        while (r-l+1)-maxf > k:
            mp[s[l]]-=1
            l+=1
        ans=max(ans,r-l+1)
       return ans
