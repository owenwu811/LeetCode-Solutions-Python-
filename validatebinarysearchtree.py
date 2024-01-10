

#Given the root of a binary tree, determine if it is a valid binary search tree (BST).

#A valid BST is defined as follows:

#The left subtree
# of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.


#my solution - python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return (validate(node.left, left, node.val) and validate(node.right, node.val, right))

        return validate(root, float('-inf'), float('inf'))


#practice run #2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True
            if not (node.val > small and node.val < large):
                return False
            return (dfs(node.left, small, node.val) and dfs(node.right, node.val, large))
        
        return dfs(root, float('-inf'), float('inf'))
