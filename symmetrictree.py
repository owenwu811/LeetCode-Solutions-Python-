
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


#better notes:

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(root1, root2):
            if root1 == None and root2 == None: #we haven't returned False but have hit bottom of both copies of trees, so we are symmmetric up to this point
                return True
            if root1 == None or root2 == None or root1.val != root2.val: #a single imbalance at each level indicates the entire tree is not 100% symmetric
                return False
            return solve(root1.left, root2.right) and solve(root1.right, root2.left) #python has lazy and operator, so it won't evaluate solve(root1.right, root2.left) until all solve(root1.left, root2.right) calls have finished first aka hit base case and returned True. It evaluates its operands from left to right and stops evaluating as soon as it encounters a False value because it knows that the ENTIRE EXPRESSION will be False REGARDLESS of the values of the REMAINING operands.
        return solve(root, root)

#when we backtrack, we go up one level, and then we move both root1 and root2 inwards towards each other instead of outwards to symbolize the 2nd solve(root1.right, root2.left)

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

#4/26/24 refresher:

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None or root1.val != root2.val:
                return False
            return solve(root1.left, root2.right) and solve(root1.right, root2.left)


        return solve(root, root)


#4/27/24:

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
                return False #one imbalance means entire thing is imbalanced
            return solve(root1.left, root2.right) and solve(root1.right, root2.left)
        return solve(root, root)

#4/29/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None or root1.val != root2.val: #if root1 or root2 dosen't work - it has to be if root1 == None or root2 == None
                return False
            return f(root1.left, root2.right) and f(root1.right, root2.left)
        return f(root, root)


#this one works too:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 and not root2 or root2 and not root1 or root1.val != root2.val:
                return False
            return f(root1.left, root2.right) and f(root1.right, root2.left)
        return f(root, root)
