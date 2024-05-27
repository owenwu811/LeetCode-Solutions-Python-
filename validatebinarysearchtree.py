

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


#1/19/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            #if there is no root in the tree, it dosen't violate the bst property, so it's technically considered a valid binary search tree
            if root is None:
                return True
            #if any of the levels violate the bst property, then the entire tree is not 100% balanced
            if not (lowerbound < root.val < upperbound):
                return False
            #traversing down both left and right subtrees to check each level 
            return (dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound))
        return dfs(root, float('-inf'), float('inf'))


#1/21/24 practice solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            
            return dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound)
        

    
        return dfs(root, float("-inf"), float("inf"))
        


#1/24/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return (dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound))
        return dfs(root, float('-inf'), float('inf'))


#1/25/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return (dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound))
        return dfs(root, float('-inf'), float('inf'))


#1/31/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            #we will check every level of the left and right subtrees and return a boolean for each level - if False, we can already return False as the entire result, which will trigger the and to return False since it's lazy, which will propogate to the original recursive call
            return (valid(root.left, lowerbound, root.val) and valid(root.right, root.val, upperbound))
        
        return valid(root, float('-inf'), float('inf'))



#2/6/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root, lowerbound, upperbound):
            if not root: #technically not violating the constraints of a valid bst, so return True for this level
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return f(root.left, lowerbound, root.val) and f(root.right, root.val, upperbound)
        return f(root, float('-inf'), float('inf'))

#2/11/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound): #checking each level of bst 
                return False
            return f(root.left, lowerbound, root.val) and f(root.right, root.val, upperbound)
        return f(root, float('-inf'), float('inf'))


#2/14/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root, lowerbound, upperbound):
            #only will be true in 1st turn
            if not root:
                return True
            #checking each level of BST
            if not (lowerbound < root.val < upperbound):
                return False
            #lazy and - right subtree will only evaluate if and only if left subtree returns true for all of it's layers
            return f(root.left, lowerbound, root.val) and f(root.right, root.val, upperbound)
        return f(root, float('-inf'), float('inf'))


#2/23/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return f(root.left, lowerbound, root.val) and f(root.right, root.val, upperbound)
        return f(root, float('-inf'), float('inf'))

#2/29/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root, lower, upper):
            if not root: #will only be True on 1st or last turn
                return True
            if not (lower < root.val < upper): #every level of tree
                return False
            return f(root.left, lower, root.val) and f(root.right, root.val, upper)
        return f(root, float('-inf'), float('inf'))


#3/6/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return (dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound))
        return dfs(root, float('-inf'), float('inf'))


#3/14/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound) #lowerbound and upperbound change!
        return dfs(root, float('-inf'), float('inf'))


#3/20/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root, lowerbound, upperbound):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return f(root.left, lowerbound, root.val) and f(root.right, root.val, upperbound)
        return f(root, float('-inf'), float('inf'))
            

#5/7/24 refresher (missed):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(lowerbound, upperbound, root):
            if not root:
                return True
            if not (lowerbound < root.val < upperbound):
                return False
            return f(lowerbound, root.val, root.left) and f(root.val, upperbound, root.right) #lowerbound and upperbound change!, so you can't just use float('-inf')! you have to use lowerbound and upperbound variable

        return f(float('-inf'), float('inf'), root)

#5/8/24 refresher (almost missed):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(lower, upper, root):
            if not root: 
                return True
            if not (lower < root.val < upper): 
                return False
            return f(lower, root.val, root.left) and f(root.val, upper, root.right)

        return f(float('-inf'), float('inf'), root) #do not forget return here at the end! you will fail the same test cases!


#5/10/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(lower, upper, root):
            if not root: 
                return True
            if not (lower < root.val < upper):
                return False
            return f(lower, root.val, root.left) and f(root.val, upper, root.right)


        return f(float('-inf'), float('inf'), root)


#5/20/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(lower, upper, root):
            if not root: return True
            if not (lower < root.val < upper):
                return False
            return f(lower, root.val, root.left) and f(root.val, upper, root.right)

        return f(float('-inf'), float('inf'), root)


#5/27/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(lower, upper, root):
            if not root:
                return True
            if not (lower < root.val < upper):
                return False
            return f(lower, root.val, root.left) and f(root.val, upper, root.right)
        return f(float('-inf'), float('inf'), root)
            
            
            
