
104. Maximum Depth of Binary Tree
Easy
11.9K
195
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100



#recursive solution (Python):


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    def maxDepth(self, root: Optional[TreeNode]) -> int: #we are given the maxDepth method as part of the Solution class
        if root is None: #base case of recursion
            return 0
        left = 1 + self.maxDepth(root.left) #if this is called, the program moves down to the left one node and then returns to line 41 to call the method from the top again. if we are on a leaf node, the recursion dosen't determine this until we return back to line 41 and 42 to determine if this is a base case.
        right = 1 + self.maxDepth(root.right)
        return max(left, right) 
            
        
        
      # when trying to determine the depth for the left child of D (which doesn't exist), the method call becomes self.maxDepth(None) because D.left is None.
      # when a leaf node returns 0, it's just that particular next iteration returning 0 where self.maxDepth(None) not overriding the entire previous left historical height
      # if you switch the order of lines 44 and 45, the result will still be correct

#refresher solution (10/25/23):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

#my solution 11/11/23:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left) #these are the recursive calls
        right = self.maxDepth(root.right) #these are the recursive calls
        return max(left, right) + 1 #returning the bigger of the two + 1 because we are one above 


#my solution 12/25/23 - good explanation of how recursion works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 #returns 0 back as the value of the maxDepth function back to the function call that started it after hitting bottom of tree aka base case
        left = self.maxDepth(root.left) #finish getting to bottom of left node, so return 0 as the last function call, and we know how tall left subtree is, so move onto next line right = self.maxDepth(root.right) and do the same thing
        right = self.maxDepth(root.right) #after we finish getting to the bottom of the right node, we return 0 from the base case, and we know how tall we are, so, in the next line, we add one to get to where we are, and then we pick the bigger of the two 
        return 1 + max(left, right)


#2/16/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l, r)
