# https://leetcode.com/problems/reverse-prefix-of-word/?envType=daily-question&envId=2024-05-01

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        flag = False
        for c in word:
            stack.append(c)
            if c == ch: 
                flag = True
                break
        if not flag: return word
        if len(stack) == len(word): return word[::-1]
        return ''.join(stack[::-1]) + word[len(stack):]
        # index = 0
        # for c in word:
        #     if c == ch:
        #         break
        #     index += 1
        # if index == len(word): return word
        # elif index == len(word) - 1: return word[::-1]
        # return word[:index + 1][::-1] + word[index + 1:]
