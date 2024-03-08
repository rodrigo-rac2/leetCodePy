## https://leetcode.com/problems/palindrome-pairs/

class Solution:
    def isPalindrome(self, word):
        return word == word[::-1]
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        output = []
        for word in words:
            for w in words:
                if word != w and self.isPalindrome(word + w):
                    output.append([words.index(word),words.index(w)])
        return output
