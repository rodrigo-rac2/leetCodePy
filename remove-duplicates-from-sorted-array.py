# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dups = []
        for i in range(len(nums)):
            if nums[i] not in dups: 
                dups.append(nums[i])
        for index in range(len(dups)):
            nums[index] = dups[index]
        return len(dups)
