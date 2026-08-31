class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        i=len(nums)-1
        ans=[0]*len(nums)


        while(l<=r):
            lsq=nums[l]*nums[l]
            rsq=nums[r]*nums[r]
            if lsq>=rsq:
                ans[i] = lsq
                l+=1
            else:
                ans[i] = rsq
                r-=1
            i-=1
        return ans