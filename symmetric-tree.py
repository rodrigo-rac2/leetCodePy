# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not l and not r: return True
        elif not l or not r or l.val != r.val: return False
        return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right): return True
        return self.isMirror(root.left, root.right)
