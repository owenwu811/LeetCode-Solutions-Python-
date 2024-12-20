

#156
#medium

#Given the root of a binary tree, turn the tree upside down and return the new root.

#You can turn a binary tree upside down with the following steps:

#The original left child becomes the new root.
#The original root becomes the new right child.
#The original right child becomes the new left child.


#correct python3 solution (could not solve):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        if not root.left:
            return root
        cur = self.upsideDownBinaryTree(root.left)
        h = root.left
        h.left = root.right
        h.right = root
        root.left = root.right = None
        return cur
