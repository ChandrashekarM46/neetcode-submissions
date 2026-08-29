class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      mp={}
      freq=[]
      for num in nums:
        mp[num]=mp.get(num,0)+1
      
      s = sorted(mp,key=mp.get,reverse=True)
      return s[:k]
