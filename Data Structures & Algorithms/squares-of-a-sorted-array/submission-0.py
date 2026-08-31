class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        ans=[]

        while(l<=r):
            lsq=nums[l]*nums[l]
            rsq=nums[r]*nums[r]
            if lsq>=rsq:
                ans.append(lsq)
                l+=1
            else:
                ans.append(rsq)
                r-=1
        return ans[::-1]