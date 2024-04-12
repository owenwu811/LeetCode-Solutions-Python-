#Given the roots of two binary trees p and q, write a function to check if they are the same or not.

#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#p = [1,2,3], q = [1,2,3] - output True


#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None: #using and instead of or results in a NoneType error 
            return p == q
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #we dig down left all the way first because of the way python has lazy and that dosen't evaluate until completely True
