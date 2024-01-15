# problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            l_s = len(stack)
            if l_s == 0 or s[i] != stack[l_s - 1]: 
                stack.append(s[i])
            else: 
                stack.pop()
            
        return ''.join(stack)
        
