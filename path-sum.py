# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        allPath = []
        if root is None:
            return []
        self.find_all_paths_recursive(root, [], allPath)
        return allPath

    def find_all_paths_recursive(self, currNode, currPath, allPath):
        if currNode is None:
            return 
        currPath.append(currNode.val)
        if currNode.left is None and currNode.right is None:
            allPath.append(list(currPath))
        # traverse left sub tree
        self.find_all_paths_recursive(currNode.left, currPath, allPath)
        # traverse right sub tree
        self.find_all_paths_recursive(currNode.right, currPath, allPath)
        del currPath[-1]

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        allPaths = self.binaryTreePaths(root)
        print(allPaths)
        for path in allPaths:
            if sum(path) == targetSum: return True
        return False
