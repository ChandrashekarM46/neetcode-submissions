class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     if not nums:
        return 0
     new=sorted(set(nums))
     maxl=1
     curr=1

     for i in range(1,len(new)):
        if new[i]==new[i-1]+1:
            curr+=1
        else:
            curr = 1

        maxl=max(maxl,curr)
     
     return maxl