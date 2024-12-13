
#1123
#medium

#Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

#Recall that:

#The node of a binary tree is a leaf if and only if it has no children
#The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
#The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

#Input: root = [3,5,1,6,2,0,8,null,null,7,4]
#Output: [2,7,4]
#Explanation: We return the node with value 2, colored in yellow in the diagram.
#The nodes coloured in blue are the deepest leaf-nodes of the tree.
#Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        #print(res)
        lca = res[-1]
        #print(lca)
        self.cur = []
        def g(root):
            if not root:
                return 
            self.cur.append(root.val)
            g(root.left)
            g(root.right)


        g(root)
        print(lca, self.cur)
        for l in lca:
            if l not in self.cur:
                return None
        def f(root):
            if not root:
                return None  
            if root.val in lca:
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
