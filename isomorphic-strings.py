#  https://leetcode.com/problems/isomorphic-strings/

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         iso_dict = {}
#         for i in range(len(s)):
#             if (s[i] not in iso_dict.keys()) and (t[i] not in iso_dict.values()): iso_dict[s[i]] = t[i]
#             elif (s[i] not in iso_dict.keys()) or (iso_dict[s[i]] != t[i]): return False
#         return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for char_s, char_t in zip(s, t):
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        return True
