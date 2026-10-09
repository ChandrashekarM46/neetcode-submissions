class Solution:
    def trap(self, height: List[int]) -> int:
     l,r=0,len(height)-1
     maxl=maxr=w=0
     while l<r:
        if height[l]<height[r]:
           maxl=max(maxl,height[l])
           w+=maxl-height[l]
           l+=1
        else:
            maxr=max(maxr,height[r])
            w+=maxr-height[r]
            r-=1
     return w