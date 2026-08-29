class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        st=set()
        maxl=0
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[l])
                l+=1
            st.add(s[right])
            maxl=max(maxl,right-l+1)
        return maxl

