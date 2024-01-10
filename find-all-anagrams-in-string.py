# Problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l_p = len(p)
        dict_anagrams = Counter(p)
        dictWindow = Counter(s[0:l_p])
        ans = []
        print(dictWindow)
        if dictWindow == dict_anagrams:
            ans.append(0)
        for i in range (1, len(s) - l_p + 1):
            if i > 0:
                if dictWindow[s[i-1]] > 1:
                    dictWindow[s[i-1]] -= 1
                else:
                    del dictWindow[s[i-1]]

            if dictWindow[s[i + l_p - 1]] > 0:
                dictWindow[s[i + l_p - 1]] += 1
            else:
                dictWindow[s[i + l_p - 1]] = 1

            if dictWindow == dict_anagrams:
                ans.append(i)
        return ans
