
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

        
