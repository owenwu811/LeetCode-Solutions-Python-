

#865
#medium

#Given the root of a binary tree, the depth of each node is the shortest distance to the root.

#Return the smallest subtree such that it contains all the deepest nodes in the original tree.

#A node is called the deepest if it has the largest depth possible among any node in the entire tree.

#The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

#Input: root = [3,5,1,6,2,0,8,null,null,7,4]
#Output: [2,7,4]
#Explanation: We return the node with value 2, colored in yellow in the diagram.
#The nodes coloured in blue are the deepest nodes of the tree.
#Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = deque()
        d.append(root)
        res = []
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft() 
                if cur:
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                res.append(level)
        lca = res[-1]
        print(lca)
        self.cur = []
        def g(root):
            if not root:
                return 
            self.cur.append(root.val)
            g(root.left)
            g(root.right)


        g(root)
        for l in lca:
            if l not in self.cur:
                return None
        def f(root):
            if not root:
                return None  
            for l in lca:
                if l == root.val:
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
