# problem: https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        s_length = len(s_list)
        
        if len(pattern) != s_length:
            return False

        pattern_dict = dict(zip(list(pattern), s_list))

        values_seen = set()
        for value in pattern_dict.values():
            if value in values_seen:
                return False
            values_seen.add(value)

        for i in range(s_length):
            if s_list[i] != pattern_dict.get(pattern[i]):
                return False

        return True
