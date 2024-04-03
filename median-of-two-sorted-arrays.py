# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def mergeArrays(self, nums1: List[int], nums2: List[int]) -> (List[int], int):
        nums = []
        i_n1 = 0
        i_n2 = 0
        index = 0
        while (i_n1 < len(nums1)) and (i_n2 < len(nums2)):
            if nums1[i_n1] < nums2[i_n2]: 
                nums.append(nums1[i_n1])
                i_n1 += 1
            elif nums2[i_n2] < nums1[i_n1]:
                nums.append(nums2[i_n2])
                i_n2 += 1
            else:
                nums.append(nums1[i_n1])
                nums.append(nums2[i_n2])
                i_n1 += 1
                i_n2 += 1
                index += 1
            index += 1
        while (i_n1 < len(nums1)):
            nums.append(nums1[i_n1])
            i_n1 += 1
            index += 1
        while (i_n2 < len(nums2)):
            nums.append(nums2[i_n2])
            i_n2 += 1
            index += 1
        return (nums, index)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums, index = self.mergeArrays(nums1, nums2)
        if not nums: return 0
        if not index % 2:
            index = index // 2
            return (nums[index] + nums[index-1]) / 2
        else:
            index = index // 2
            return (nums[index])
        
