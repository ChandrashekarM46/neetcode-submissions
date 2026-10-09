class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        st=set()
        maxl=0

        while r<len(s):
            if s[r] in st:
                st.remove(s[l])
                l+=1
            else:
                st.add(s[r])
                maxl=max(maxl,r-l+1)
                r+=1
        return maxl
