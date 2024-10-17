
#112
#easy


#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

#A leaf is a node with no children.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = []
        self.ans = []
        def f(root):
            if not root:
                return 0
            self.res.append(root.val)
            l = f(root.left)
            r = f(root.right)
            if not root.left and not root.right:
                if sum(self.res) == targetSum:
                    self.ans.append(True)
            self.res.pop()
            return root.val + l + r
        f(root)
        if self.ans:
            return self.ans[0]
        return False
