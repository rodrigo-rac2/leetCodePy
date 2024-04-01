# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mountBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        l = len(nums)
        index = l // 2
        top = TreeNode(nums[index])
        top.left = self.mountBST(nums[0:index])
        top.right = self.mountBST(nums[index+1:])
        return top

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        head = self.mountBST(nums)
        return head
