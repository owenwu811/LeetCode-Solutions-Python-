#1973
#medium


#Given the root of a binary tree, return the number of nodes where the value of the node is equal to the sum of the values of its descendants.

#A descendant of a node x is any node that is on the path from node x to some leaf node. The sum is considered to be 0 if the node has no descendants.

#Input: root = [10,3,4,2,1]
#Output: 2
#Explanation:
#For the node with value 10: The sum of its descendants is 3+4+2+1 = 10.
#For the node with value 3: The sum of its descendants is 2+1 = 3.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def f(root):
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            if root.val == l + r:
                self.res += 1
            return root.val + l + r
        f(root)
        return self.res
