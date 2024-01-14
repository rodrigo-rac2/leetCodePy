# Problem: https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # words = s.split()
        # word = words[len(words) - 1]
        # return len(word)
        k = len(s) - 1
        while(s[k] == " "):
            s = s[:len(s)-1]
            k -= 1
        l_s = len(s)
        if l_s == 1:
            if s[0] != " ":
                return 1
            else:
                return 0
        counter = 0
        for i in range(l_s, 0, -1):
            if s[i - 1] == " ":
                break
            else: 
                counter = counter + 1
        return counter
