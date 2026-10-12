class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp={}
        res=[]
        for num in nums:
            mp[num]=mp.get(num,0)+1
            if num not in res and mp[num]>len(nums)/3:
              res.append(num)   
        return res