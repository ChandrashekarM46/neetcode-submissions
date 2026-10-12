class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
         cand1=cand2=count1=count2=0
         f1=f2=0
         n=len(nums)
         res=[]
         for num in nums:
            if num==cand1:
                count1+=1
            elif num==cand2:
                count2+=1
            elif count1==0:
                cand1=num
                count1=1
            elif count2==0:
                cand2=num
                count2=1
            else:
                count1-=1
                count2-=1
        
         
         for num in nums:
            if num==cand1:
                f1+=1
                if num not in res and f1>n//3:
                    res.append(num)
            elif num==cand2:
                f2+=1
                if num not in res and f2>n//3:
                    res.append(num)
         return res
        
            
            