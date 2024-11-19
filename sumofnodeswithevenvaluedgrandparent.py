

#1315
#medium

#Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

#A grandparent of a node is the parent of its parent if it exists.

#Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
#Output: 18
#Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def f(root):
            if not root:
                return 
            if root.val % 2 == 0:
                if root.left and root.left.left:
                    print(root.val, root.left.left.val)
                    self.res += root.left.left.val
                if root.right and root.right.right:
                    print(root.val, root.right.right.val)
                    self.res += root.right.right.val
                if root.right and root.right.left:
                    print(root.val, root.right.left.val)
                    self.res += root.right.left.val
                if root.left and root.left.right:
                    print(root.val, root.left.right.val)
                    self.res += root.left.right.val
            l = f(root.left)
            r = f(root.right)
        f(root)
        return self.res
