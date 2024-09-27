

#94
#easy

#Given the root of a binary tree, return the inorder traversal of its nodes' values.


#my own solution using python3:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def f(root):
            if not root:
                return
            root.left = f(root.left)
            self.res.append(root.val)
            root.right = f(root.right)
            if not root.left and not root.right:
                return None
        f(root)
        return self.res
