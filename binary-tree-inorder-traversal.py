# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     r = []
    #     if not root: return
    #     if root.left:
    #         r += self.inorderTraversal(root.left)
    #     r.append(root.val)
    #     if root.right:
    #         r += self.inorderTraversal(root.right)
    #     return r
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        current = root
    
        while current or stack:
            # Reach the left most Node of the current Node
             while current:
                # Place pointer to a tree node on the stack 
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left
            # Current must be None at this point
            current = stack.pop()
            result.append(current.val)  # Add the node value to result
            current = current.right     # We have visited the node and its left subtree.
                                        # Now, it's right subtree's turn    
        return result
