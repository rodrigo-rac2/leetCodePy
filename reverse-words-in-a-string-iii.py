# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reverse_word_list = []
        for word in words:
            reverse_word_list.append(word[::-1])
        return " ".join(reverse_word_list)
