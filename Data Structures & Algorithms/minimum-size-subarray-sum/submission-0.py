class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
     l=0
     minl=float("inf")
     tsum=0
     for r in range(len(nums)):
        tsum+=nums[r]
        while tsum>=target:
            minl=min(minl,r-l+1)
            tsum-=nums[l]
            l+=1
     return 0 if minl==float("inf") else minl
        