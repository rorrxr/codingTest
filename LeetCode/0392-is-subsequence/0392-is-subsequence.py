class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        
        s_index = 0
        t_index = 0
        
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        
        return s_index == len(s)