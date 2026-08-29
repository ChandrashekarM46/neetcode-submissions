class Solution:
    def isValid(self, s: str) -> bool:
        char_map={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        st=[]

        for b in s:
           if len(st)>0 and b in char_map and st[-1] == char_map[b]:
             st.pop()
           else:
            st.append(b)

        return len(st)==0