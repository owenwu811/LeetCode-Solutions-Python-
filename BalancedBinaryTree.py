110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

Solution:

#balanced binary tree basically means that one tree must not be shorter or taller by the other tree by more than 1 node vertically

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1 #recursive calls trasversing down binary tree
        
        def check_balance(node): #each recursive call compares if the left and right heights are differing by more than 1
            if node is None:
                return True
            
            left_height, right_height = get_height(node.left), get_height(node.right) #call line 3 function again except trasversing down one node to the left 
            
            if abs(left_height - right_height) > 1: #the left and right trees have heights that differ by more than one node vertically
                return False
            
            return check_balance(node.left) and check_balance(node.right)
        
        return check_balance(root)


#another solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #initializes a list res with a single element, 1.
        #Lists are mutable in Python, so the code uses a list with a single element to be able to modify its value inside the maxDepth function.
        res = [1]
        def maxDepth(root):
            if root is None:
                return False
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            if abs(right - left) > 1:
                res[0] = False
            return 1 + max(left,right)
        maxDepth(root)
        if res[0] == 1:
            return True 
        else:
            return False

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def f(root):
            if root is None:
                return 0
            l = f(root.left)
            r = f(root.right)
            if abs(r - l) > 1:
                res[0] = False
            #without the line return 1 + max(l, r), the abs function would have no integers to actually compute the difference between the r and l subtrees as the line provides the height of the current node as an integer + 1 to account for the current node itself 
            return 1 + max(l, r) #this line is used to tell us the current height aka keep track of where we are in the tree so that, in the next iteration, we can actually compare r and l as integers in the abs function
        f(root)
        return res[0]

#2/4/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(root):
            if root is None:
                return 0 #to indicate that the height of a None level is 0
            l = f(root.left)
            r = f(root.right)
            if abs(r - l) > 1: #absolute value!!!!
                res[0] = False
            return 1 + max(l, r) #where we currently are will be returned as one above to the function call that started it
        res = [True]
        f(root)
        return res[0]
        
