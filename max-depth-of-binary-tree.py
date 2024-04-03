# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth = 0
        # if not root: return 0
        # elif root.left == None and root.right == None: 
        #     return 1
        # elif root.left == None: 
        #     depth = 1 + self.maxDepth(root.right)
        # elif root.right == None: 
        #     depth = 1 + self.maxDepth(root.left)
        # else: 
        #     depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # return depth
        if not root:
            return 0
        
        stack = [(root, 1)]  # Stack of (node, depth)
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return max_depth
