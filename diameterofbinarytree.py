
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




#1/31/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.val = max(self.val, left + right)
            return 1 + max(left, right)



        self.val = 0
        dfs(root)
        return self.val


#2/8/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)

        self.res = 0
        dfs(root)
        return self.res

#important note: we can't just call diameterOfBinaryTree without the def dfs() because the first - return 1 + max(l, r) - would ovveride the second, so the second wouldn't even get executed. To illustrate this, look at the incorrect solution below:

#class Solution:
#    def diameterOfBinaryTree(self, root: TreeNode) -> int:
#        def dfs
#        if root is None:
#            return 0
#        l = diameterOfBinaryTree(root.left)
#        r = diameterOfBinaryTree(root.right)
#        self.res = max(self.res, l + r)
#        return 1 + max(l, r)

#    self.res = 0
#    diameterOfBinaryTree(root)
#    return self.res

#3/5/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def f(root):
            if root == None:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)

        self.res = 0
        f(root)
        return self.res
        

#3/17/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def f(root):
            if root == None:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, r + l)
            return 1 + max(l, r)
        



        self.res = 0
        f(root)
        return self.res

#3/24/24:

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
            l = f(root.left) #because we want to go from the left side of the tree to the right, this is depth first search
            r = f(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)

        self.res = 0
        f(root)
        return self.res


#5/6/24 missed:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def f(root):
            if root == None:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, l + r) #without self, the res would always b 0 even if you passed it in because it wouldn't global!
            return 1 + max(l, r)
            
        self.res = 0 #without self, the res would always b 0 even if you passed it in!
        f(root)
        return self.res #without self, the res would always b 0 even if you passed it in! you would just get the res declared outside of the recursive function!


#5/7/24 practice:

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


#5/18/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def f(root):
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)

        
        self.res = 0
        f(root)
        return self.res

#6/17/24 review:

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
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        
        f(root)
        return self.res
        
