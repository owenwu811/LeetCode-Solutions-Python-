
#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

#python3 solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True #the idea is that if the smaller tree is empty, then technically the bigger tree matches the smaller tree -  this is because any tree contains an empty tree as a subtree
        if not root: return False 
        if self.same(root, subRoot):  #we know that both Trees exist, so we now have to compare all children of both trees to make sure exactly the same 
            return True
        #just traversing the bigger tree that's trying to cater a part to smaller tree because either left OR right side of bigger tree can match smaller tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #calling each level of bigger tree
    def same(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val: #still have to dig down left in both subtrees first to make sure child nodes are also the same and same value
            return self.same(p.left, q.left) and self.same(p.right, q.right)
        return False #we know this smaller part of root and entire subroot didn't match, so we have to keep traversing down bigger root tree by going back to line 21 to see if another part of bigger tree matches smaller tree 

#4/29/24 refresher:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def same(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.same(p.left, q.left) and self.same(p.right, q.right)
        return False


#refresher again:

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False
        if self.solve(s, t):
            return True
        #not entirely true, so move down left in the bigger subtree and try again
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def solve(self, p, q):
        if p == None and q == None: #base case when we hit empty leaf on both trees
            return True
        if p and q and p.val == q.val: #just because one node matches dosen't mean we don't need to check rest of subtree
            return self.solve(p.left, q.left) and self.solve(p.right, q.right)
        return False


#5/1/24 refresher:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot and root: return True
        if not root and subRoot: return False
        if self.solve(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def solve(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val: #just because one level is matching dosen't mean we don't need to compare children of both trees as well
            return self.solve(p.left, q.left) and self.solve(p.right, q.right)
        return False

#5/2/24:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        #we want to start at the root of both trees
        #we want to compare the values. If the values are the same, then we need to traverse left in both trees, and then traverse right in both trees.
        #if the values don't match, then we need to move down left in root, and try the process again
        if not subRoot: return True 
        if not root: return False
        if self.solve(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def solve(self, p, q): #recursive calls where we traverse down both trees
        if p == None and q == None: #reached root of Both trees, so return True
            return True
        if p and q and p.val == q.val:
            return self.solve(p.left, q.left) and self.solve(p.right, q.right)
        return False #we found a mismatch between the two trees, so move down left in bigger tree and try again


#5/9/24 refresher:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        #a part of big that is the same as small
        if not subRoot: return True
        if not root: return False
        if self.solve(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #or here, not and, because either the left or right part of big tree could be a footprint of small
    def solve(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.solve(p.left, q.left) and self.solve(p.right, q.right)
        return False


#5/21/24 practice:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        if self.solve(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def solve(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.solve(p.left, q.left) and self.solve(p.right, q.right)
        return False
