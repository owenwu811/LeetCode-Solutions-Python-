#1026
#medium


#Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

#A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

#Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
#Output: 7
#Explanation: We have various ancestor-node differences, some of which are given below :
#|8 - 3| = 5
#|3 - 7| = 4
#|8 - 1| = 7
#|10 - 13| = 3
#Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


#my own solution using python3:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = []
        def f(root, cur):
            if not root:
                return
            cur.append(root.val)
            root.left = f(root.left, cur)
            root.right = f(root.right, cur)
            if not root.left and not root.right:
                self.res.append(cur.copy())
            cur.pop()
        f(root, [])
        ans = 0
        for r in self.res:
            ans = max(ans, max(r) - min(r))
        return ans
            



     
