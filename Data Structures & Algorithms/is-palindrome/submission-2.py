class Solution:
    def isPalindrome(self, s: str) -> bool:
       ns=s.lower()
       i=0
       j=len(s)-1

       while i<j:
         while i<j and not ns[i].isalnum():
            i+=1
         while i<j and not ns[j].isalnum():
            j-=1

         if ns[i]!=ns[j]:
            return False
         
         i+=1
         j-=1
       
       return True