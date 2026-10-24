class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        h=sum(nums)

        while l<h:
            mid=(l+h)//2
            cur=0
            arr=1

            for num in nums:
                if num+cur>mid:
                    cur=0
                    arr+=1
                cur+=num
            
            if arr<=k:
                h=mid
            else:
                l=mid+1
        return l