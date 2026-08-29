class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l=0
        maxl=0
        res=[]
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>maxl:
             res.append(i)
            maxl=max(maxl,heights[i])
        res.reverse()
        return res
