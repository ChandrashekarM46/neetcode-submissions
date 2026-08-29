class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      operators='*-+/'
      st=[]
      ans=0

      for token in tokens:
        if token in operators and len(st)>1:
            t2=int(st.pop())
            t1=int(st.pop())
            if token=='+':
                ans=t1+t2
            if token=='-':
                ans=t1-t2
            if token=='*':
                ans=t1*t2
            if token=='/':
               ans=int(t1/t2)
            st.append(ans)
        else:    
            st.append(token)  
      return int(st[-1])