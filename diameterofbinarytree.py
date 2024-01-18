
#Given the root of a binary tree, return the length of the diameter of the tree.

#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#The length of a path between two nodes is represented by the number of edges between them.

#Input: root = [1,2,3,4,5]
#Output: 3
#Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


#my solution - python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def f(root):
            #base case where we hit bottom of tree on either side, so return 0 for that height back to f passed back as the value of the function call that started it (either l or r) - if l, then we finished all the left function calls, and do the same thing with the right side
            if root is None:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, l + r)
            #we need to return this as the result of the f function itself since we've finished traversing to the bottom of left and right trees at this point, so we know the heights of both, and we need to find where we are currently, so we add 1. this is a seperate part from result, which is updated as max above. 
            return 1 + max(l, r)

        f(root)
        return self.res



#1/7/24 refresher solution - python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def f(root):
            if root is None:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        f(root)
        return self.res



#1/11/24 refresher solution - python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def f(root):
            if root is None:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)


        self.res = 0
        f(root)
        return self.res


#1/17/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.val = 0
        def f(root):
            if root is None:
                return 0
            left = f(root.left)
            right = f(root.right)
            self.val = max(self.val, left + right)
            return 1 + max(left, right) #returns to the function call that caused it - either left or right, and then left or right calls def f(root) again

        f(root)
        return self.val
