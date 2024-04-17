# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        def dfs(node, path):
            if node is None:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                ret.append("->".join(path))
            else:
                dfs(node.left, path.copy())
                dfs(node.right, path.copy())
        dfs(root, [])
        return ret

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.getPaths(root)
