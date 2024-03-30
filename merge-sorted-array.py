# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        if n == 0: 
            nums1 = nums1
        elif m == 0:
            while index2 < n:
                nums1[index1] = nums2[index2]
                index2 += 1
                index1 += 1
        else:
            while index1 < m + n and index2 < n:
                print(index1, nums1, nums1[index1])
                print(index2, nums2, nums2[index2])
                print()
                if (index1 >= m):
                    while index2 < n:
                        nums1[index1] = nums2[index2]
                        index2 += 1
                        index1 += 1
                elif (nums1[index1] >= nums2[index2]):
                    nums1.insert(index1, nums2[index2])
                    nums1.pop()
                    m += 1
                    index2 += 1
                else:
                    index1 += 1
