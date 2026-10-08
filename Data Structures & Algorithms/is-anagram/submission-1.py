class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp_s={}
        mp_t={}
        for c in s:
            mp_s[c]=mp_s.get(c,0)+1
        for c in t:
            mp_t[c]=mp_t.get(c,0)+1
        return mp_s==mp_t