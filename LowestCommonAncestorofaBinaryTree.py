
#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


#my solution: python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l is not None and r is not None: return root
        elif l is not None and r == None: #In the line elif l and not r:, l represents the result obtained from the left subtree. If l is not None, it means one of p or q has been found in the left subtree.
            return l
        elif r is not None and l == None: return r
        elif l == None and r == None: return None

#practice run 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #we want to find the lowest common parent of p and q 
        #the deepest node that is a parent of p and q meaning p and q is a child of this node not necessarily directly a child
        if root == None or root == p or root == q:  #if root == None, then return root means return None!!!!
            return root #this just represents the base case for one of the two recursive calls (starting from l == self. or r == self.)? meaning that if the final state of l is None but the final state of r is not None, we still return r as the final result?
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l is not None and r is not None: return root
        elif l is not None and r == None: return l #because l equals to p or q
        elif r is not None and l == None: return r
        else: return None
