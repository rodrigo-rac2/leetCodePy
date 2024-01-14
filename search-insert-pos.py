# problem: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n_l = len(nums)
        for i in range(n_l):
            if nums[i] >= target:
                return i
        return n_l
