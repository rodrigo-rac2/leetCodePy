# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [(root, 1)]
        minDepth = 100000
        while stack:
            node, depth = stack.pop()
            if node:
                if not node.left and not node.right: # leaf
                    minDepth = min(minDepth, depth)
                stack.append((node.right, 1 + depth))
                stack.append((node.left, 1 + depth))

        return minDepth
