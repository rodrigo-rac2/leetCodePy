# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        l_s_pre = len(s)
        l_s_post = -1
        while l_s_pre != l_s_post:
            l_s_pre = len(s)
            if l_s_pre < 2: return s
            if abs(ord(s[l_s_pre - 2]) - ord(s[l_s_pre - 1])) == 32:
                s = s[:l_s_pre - 2]
            for i in range(l_s_pre - 2):
                if abs(ord(s[i]) - ord(s[i+1])) == 32:
                    s = s[:i] + s[i+2:]
                    break
            l_s_post = len(s)
        return s
