class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        t_sum=(n*(n+1))//2
        a_sum=sum(nums)

        return t_sum-a_sum