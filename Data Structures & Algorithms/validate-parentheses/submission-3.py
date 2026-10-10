class Solution:
    def isValid(self, s: str) -> bool:
        mp={
            '}':'{',
            ']':'[',
            ')':'('
        }
        st=[]
        for p in s:
            if p in mp and len(st)>0 and mp[p]==st[-1]:
                st.pop()
            else:
                st.append(p)
        return len(st)==0