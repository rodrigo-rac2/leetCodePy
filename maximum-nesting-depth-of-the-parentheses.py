# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-05-01

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_l = 0
        for c in s:
            if c == '(': stack.append(c)
            elif c == ')': 
                l = len(stack)
                if l > max_l: max_l = l
                stack.pop()
        return max_l
        
