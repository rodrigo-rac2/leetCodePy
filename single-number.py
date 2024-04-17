# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
        # candidate = []
        # for num in nums:
        #     if num in candidate: candidate.remove(num)
        #     else: candidate.append(num)
        # return candidate[0]
