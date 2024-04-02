# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

class Solution:
    # # def removeFirstOccurenceOfSubstring(self, s: str, part: str) -> str:
    #     part_l = len(part)
    #     s_l = len(s)
    #     response = ""
    #     for i in range(s_l):
    #         if part == s[i:i+part_l]: 
    #             response += s[i+part_l:]
    #             break
    #         else: response += s[i]
    #     return response

    # def removeOccurrences(self, s: str, part: str) -> str:
    #     temp = self.removeFirstOccurenceOfSubstring(s, part)
    #     while(part in temp): 
    #         temp = self.removeFirstOccurenceOfSubstring(temp, part)
    #     return temp
    def removeOccurrences(self, s: str, part: str) -> str:
        test = True
        while(test):
            test = False
            i = s.find(part)
            if i != -1:
                s = s[:i] + s[i+len(part):]
                test = True
        return s
