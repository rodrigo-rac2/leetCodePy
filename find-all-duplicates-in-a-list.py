# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numsDict = Counter(nums)
        duplicate_list = []
        for key in numsDict:
            candidate = numsDict[key]
            if candidate == 2:
                duplicate_list.append(key)
        return duplicate_list
