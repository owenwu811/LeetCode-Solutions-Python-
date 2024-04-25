
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

#           1
#         2   2
#       3  4 4  3

#output = True

#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None or root1.val != root2.val:
                return False
            return solve(root1.left, root2.right) and solve(root1.right, root2.left)
        return solve(root, root)

  #you first dig down with root1:

#      1
#   2
# 3

#while also digging down with root2:

#      1
#         2
#            3

#when we hit the base case, we have reached empty nodes on both sides, so if we haven't returned False, then it is symmetric up to this point
#we then backtrack, so root1 becomes:

#      1
#   2

#and root2 becomes:

#   1 
#     2

#and then root1 goes right and root2.goes left

#so root1 becomes:

#       1
#    2
#       4

#and root2 becomes:

#     1
#         2
#     4
