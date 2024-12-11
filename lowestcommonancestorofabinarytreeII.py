

#1644
#medium

#Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

#According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Output: 3
#Explanation: The LCA of nodes 5 and 1 is 3.

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.cur = []
        def g(root):
            if not root:
                return 
            self.cur.append(root.val)
            g(root.left)
            g(root.right)


        g(root)
        if p and q:
            if p.val not in self.cur or q.val not in self.cur:
                return None
        def f(root, p, q):
            if not root:
                return
            if root and p and q:
                if root.val == p.val or root.val == q.val:
                    return root
            print(root.val, p.val, q.val)
            l = f(root.left, p, q)
            r = f(root.right, p, q)
            if l and r:
                return root 
            if r and not l:
                return r
            if l and not r:
                return l
            return None
        return f(root, p, q)
