# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        window_start = 0
        window_end = k
        maxC = 0
        for i in range(k):
            if s[i] in vowels: maxC += 1
        count = maxC
        while(window_end < len(s)):
            if s[window_start] in vowels:
                count -= 1
            if s[window_end] in vowels:
                count += 1
            if maxC < count: maxC = count
            window_start += 1
            window_end += 1

        return maxC
    #  non-optimized:
    #  def maxVowels(self, s: str, k: int) -> int:
    #     vowels = ['a', 'e', 'i', 'o', 'u']
        # maxNum = 0
        # for i in range(len(s)):
        #     count = 0
        #     for c in s[i:i+k]:
        #         if c in vowels:
        #             count += 1
        #     if maxNum < count: maxNum = count
        # return maxNum
