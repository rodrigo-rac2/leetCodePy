# problem: https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictRansom = Counter(ransomNote)
        dictMagazine = Counter(magazine)
        for k in dictRansom:
            if dictRansom[k] > dictMagazine[k]:
                return False
        return True
