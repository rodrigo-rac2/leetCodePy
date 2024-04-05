# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLength(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        else: return 1 + max(self.getLength(root.left), self.getLength(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if abs(self.getLength(root.left) - self.getLength(root.right)) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
