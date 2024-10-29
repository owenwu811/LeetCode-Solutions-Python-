
#1120
#medium


#Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

#A subtree of a tree is any node of that tree plus all its descendants.

#The average value of a tree is the sum of its values, divided by the number of nodes.

#Input: root = [5,6,1]
#Output: 6.00000
#Explanation: 
#For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
#For the node with value = 6 we have an average of 6 / 1 = 6.
#For the node with value = 1 we have an average of 1 / 1 = 1.
#So the answer is 6 which is the maximum.


#correct python3 solution (could not solve):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        def f(root):
            if not root:
                return 0, 0
            lc, ls = f(root.left)
            rc, rs = f(root.right)
            tot = ls + rs + root.val
            length = lc + rc + 1
            self.res = max(self.res, tot / length)
            return length, tot
        f(root)
        return self.res
