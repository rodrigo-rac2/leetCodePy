# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        if s.isspace() or len(s) == 1: return 1
        head = 0
        tail = 0
        length = len(s)
        maxLen = 0
        while head < length:
            tail += 1
            if tail > length - 1: break
            sub = s[head:tail]
            if s[tail] in sub:
                if maxLen < len(sub): maxLen = len(sub)
                head += 1
                sub = s[head:tail+1]
                while sub.count(s[tail]) > 1: 
                    head += 1
                    sub = s[head:tail+1]
            else:
                sub = s[head:tail+1]
        if maxLen < len(sub): maxLen = len(sub)
        return maxLen
                
