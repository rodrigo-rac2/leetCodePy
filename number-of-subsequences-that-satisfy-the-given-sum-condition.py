# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def generate_all_possible_subarrays(self, arr):
        subarrays = []
        n = len(arr)
    
        # Consider all combinations of elements for lengths 1 to n
        for length in range(1, n + 1):
            for indices in combinations(range(n), length):
                subarray = [arr[i] for i in indices]
                subarrays.append(subarray)
    
        return subarrays

    def numSubseq(self, nums: List[int], target: int) -> int:
        all_subs = []
        nums.sort()
        subs = self.generate_all_possible_subarrays(nums)
        for sub in subs:
            if not sub: 
                continue
            elif min(sub) + max(sub) <= target: 
                all_subs.append(sub)

        return len(all_subs)
