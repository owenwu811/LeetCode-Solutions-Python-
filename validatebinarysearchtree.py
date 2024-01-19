

#Given the root of a binary tree, determine if it is a valid binary search tree (BST).

#A valid BST is defined as follows:

#The left subtree
# of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.


#my solution - python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return (validate(node.left, left, node.val) and validate(node.right, node.val, right))

        return validate(root, float('-inf'), float('inf'))


#practice run #2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True
            if not (node.val > small and node.val < large):
                return False
            return (dfs(node.left, small, node.val) and dfs(node.right, node.val, large))
        
        return dfs(root, float('-inf'), float('inf'))



#practice run 1/10/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(node, small, large):
            if not node:
                return True
            if not (node.val > small and node.val < large):
                return False
            return (f(node.left, small, node.val) and f(node.right, node.val, large))
        return f(root, float("-inf"), float("inf"))


#1/14/24 practice run:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root, small, large):
            if root is None:
                return True
            if not (small < root.val < large):
                return False
            return (f(root.left, small, root.val) and f(root.right, root.val, large))

        return f(root, float("-inf"), float("inf"))


#1/15/24 practice run:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            if root is None:
                return True
            #if even one level of the tree is unbalanced, return False as we need both sides of the entire tree to be balanced
            if not (root.val > lowerbound and root.val < upperbound):
                return False
            return (dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound))
        return dfs(root, float("-inf"), float("inf"))


#1/16/24 practice run:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            #if root dosen't exist meaning either the entire tree dosen't exist or we hit a child, if we haven't returned false, then assume the binary search tree is valid
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False

            return (dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound))
        return dfs(root, float("-inf"), float("inf"))


#1/18/24 practice run:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            #technically, if there is no root in the tree, it is balanced
            if root is None:
                return True
            #checking the balance status at every level we traverse down in the input tree
            if not (root.val > lowerbound and root.val < upperbound):
                return False
            #keeps digging down one subtree (left) for example until we reach the leaf of the left subtree, and if left subtree returns True then and only then do we even evaluate the right subtree because both parts of the subtree need to be balanced at every level following the bst rule 
            return (dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound))
        
        return dfs(root, float('-inf'), float('inf'))
