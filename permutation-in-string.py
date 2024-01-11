# Problem: https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_s1, l_s2 = len(s1), len(s2)
        dict_s1 = Counter(s1)
        dict_window = Counter(s2[:l_s1])
        for i in range(l_s2-l_s1+1):
            if dict_window == dict_s1:
                return True
            if i + l_s1 == l_s2: break
            if dict_window[s2[i+l_s1]] > 0:
                dict_window[s2[i+l_s1]] += 1
            else:
                dict_window[s2[i+l_s1]] = 1
            if dict_window[s2[i]] == 1:
                del dict_window[s2[i]]
            else:
                dict_window[s2[i]] -= 1
            
        return False
