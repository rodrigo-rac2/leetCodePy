# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif (stack[-1] + c) == 'AB' or (stack[-1] + c) == 'CD':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
