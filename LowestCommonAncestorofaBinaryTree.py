
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

#2/25/24:

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
        if l and r: return root
        elif l == None and r != None: return r
        elif r == None and l != None: return l
        else: return None

#2/26/24:

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
        if l == None and r: return r
        elif r == None and l: return l
        elif l and r: return root
        else: return None


#2/28/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #lowest node that is a parent of p and q
        if root == None or root == p or root == q: #we check this at every recursive call caused by l or r
            return root
        l = self.lowestCommonAncestor(root.left, p, q) 
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root #we know the lca occurs at a split
        if l and not r: return l #we know the lca occurs in the left subtree, which was returned from the if root == None or root == p or root == q check at each level or recursive call
        elif r and not l: return r
        else: return None

#3/5/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #we want to find the lowest common parent node of both p and q nodes
        if root == None or root == p or root == q: #checked at each level
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l == None and r == None: return None
        elif l == None and r: return r #in the right subtree
        elif r == None and l: return l
        elif l and r: return root


#3/9/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #we want the lowest node in the tree that has both p and q as children
        if root == None or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        elif l and not r: return l
        elif r and not l: return r
        else: return None

#3/11/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #the node that is the lowest parent of both p and q 
        if root == None or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l and not r: return l
        if r and not l: return r
        else: return None

#3/14/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #find lowest common parent of nodes p and q
        if root == None or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l and not r: return l #return the lowest one inside of the left subtree because we want to find lowest common ancestor 
        if r and not l: return r
        else: return None

#3/18/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q: #base case
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        elif l and not r: return l
        elif r and not l: return r
        else: return None


#3/23/24:

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
        if l and r: return root
        if l and not r: return l
        if r and not l: return r
        else: return None
        
#3/27/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #a node can be a descendant of itself
        if root == None or root == p or root == q: #base case
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        elif l and not r: return l #lca in left subtree and caught at the 1st line base case when root.left was root and happened to be equal to p or q
        elif r and not l: return r
        else: return None

#4/8/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#we're not returning a subtree itself! instead, we're returning the lowest common ancestor found within that subtree. This is because as we traverse the tree recursively, each call to the function is working on a subtree, and it eventually returns the lowest common ancestor found within that subtree.

#if the current node is None, we can't find the desired nodes further down the tree, and if the current node is either p or q, it must be the lowest common ancestor of p and q.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #why results of lowest is stored in variables l and r? because the result is determined when we either hit a leaf node (root becomes none) or root is equal to either p or q
        if root == None or root == p or root == q: #root can't be None AND ALSO p or q because p and q can't be None, so if we reach leaf, root is None, and we return None vs. root == p or root == q are different scenarios. 
            return root
        #we recursively search for the lowest common ancestor in the left and right subtrees. We STORE RESULTS OF LOWEST in variables l and r
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l and not r: return l
        if r and not l: return r
        else: return None


#5/1/24:

#the following works too - it dosen't just have to be left first and then right and you can also do .val comparison in base case as well:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root
        r = self.lowestCommonAncestor(root.right, p, q)
        l = self.lowestCommonAncestor(root.left, p, q)
        #r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l and not r: return l
        if r and not l: return r
        else: return None


#5/2/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root # if both l and r are not None, it means p and q are found in different subtrees, indicating that the current root is the LCA.
        if l and not r: return l
        if r and not l: return r
        else: return None

#5/3/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #we want to find the lowest common parent of p and q
        if root == None or root == p or root == q: #we want common of both p and q, so if we found a value that equals one, then that's the lowest common parent of both
            return root 
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root #l is an alrogithm that will keep running until we find the lowest common parent in the left subtree and same with right, so if they occur at a split, then return the parent
        if l and not r: return l
        if r and not l: return r
        else: return None

#5/5/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #we want the lowest common parent of p and q
        if root == None or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l and not r: return l
        if r and not l: return r
        else: return None
