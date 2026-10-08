class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=maxl=0
        nums_set=set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                l=1
                while num+l in nums_set:
                    l+=1
                maxl=max(l,maxl)
        
        return maxl

            