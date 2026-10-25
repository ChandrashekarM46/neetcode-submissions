class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
      l=max(weights)
      h=sum(weights)

      while l<h:
        mid = (l+h)//2  
        cur=0
        d=1

        for w in weights:
            if cur+w>mid:
                cur=0
                d+=1
            cur+=w
        if d<=days:
            h=mid
        else:
            l=mid+1
      return l