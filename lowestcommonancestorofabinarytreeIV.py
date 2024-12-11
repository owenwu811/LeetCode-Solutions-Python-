
#1676
#medium

#Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

#Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

#Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
#Output: 2
#Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.cur = []

        def g(root):
            if not root:
                return 
            self.cur.append(root.val)
            g(root.left)
            g(root.right)

        g(root)
        self.now = []
        for n in nodes:
            print(n.val)
            self.now.append(n.val)
        for n in self.now:
            if n not in self.cur:
                return None
        def f(root):
            if not root:
                return 
            if root.val in self.now:
                return root
            l = f(root.left)
            r = f(root.right)
            if l and r:
                return root 
            if l and not r:
                return l            
            if r and not l:
                return r  
            return None
            


        return f(root)
        
        
