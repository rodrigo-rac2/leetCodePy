# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [ c.lower() for c in s if c.isalnum() ]
        return string == string[::-1]
