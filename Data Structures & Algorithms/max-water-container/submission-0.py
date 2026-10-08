class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=w=maxw=0
        r=len(heights)-1

        while l<r:
            width=r-l
            height=min(heights[l],heights[r])
            
            w=height*width

            maxw=max(w,maxw)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return maxw