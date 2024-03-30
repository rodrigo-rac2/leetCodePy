# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        print(root)
        if not root: return 0
        elif root.left == None and root.right == None: 
            return 1
        elif root.left == None: 
            depth = 1 + self.maxDepth(root.right)
        elif root.right == None: 
            depth = 1 + self.maxDepth(root.left)
        else: 
            depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth
