# https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def print_paths(self, root):
        ret = []
        alpha_dict = {i: chr(97 + i) for i in range(26)}

        def dfs(node, path):
            if node is None:
                return
            path.append(alpha_dict[node.val])
            if node.left is None and node.right is None:
                ret.append(path[::-1])
            else:
                dfs(node.left, path.copy())
                dfs(node.right, path.copy())
        dfs(root, [])
        return ret

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        minPath = min(self.print_paths(root))
        return ''.join(minPath)
