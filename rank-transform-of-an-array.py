# https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2024-10-07

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]: 
        cp = list(set(list(arr))) #removes duplicates and re-generate the list
        cp.sort() #sort to get ranks
        ans = []
        for n in arr:
            ans.append(cp.index(n) + 1)
        return ans
