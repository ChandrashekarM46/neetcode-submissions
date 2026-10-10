class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       l=0
       mps1={}
       mps2={}

       for char in s1:
         mps1[char]=mps1.get(char,0)+1
        
       for r in range(len(s2)):
         mps2[s2[r]]=mps2.get(s2[r],0)+1

         if r-l+1 > len(s1):
            mps2[s2[l]]-=1
            if mps2[s2[l]]==0:
                del mps2[s2[l]]
            l+=1
         if mps1==mps2:
            return True
       
       return False
       