class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1={}
        counts2={}

        if len(s1)>len(s2):
            return False
        
        for c in s1:
            counts1[c]=counts1.get(c,0)+1

        l=0

        for right in range(len(s2)):
            counts2[s2[right]]=counts2.get(s2[right],0)+1

            if right-l+1>len(s1):
                counts2[s2[l]]-=1
            
                if counts2[s2[l]]==0:
                    del counts2[s2[l]]
                l+=1
        
            if counts1==counts2:
                return True
            
        return False

