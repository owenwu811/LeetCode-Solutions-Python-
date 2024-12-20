
#298
#medium

#Given the root of a binary tree, return the length of the longest consecutive sequence path.

#A consecutive sequence path is a path where the values increase by one along the path.

#Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res, self.cur = [], []
        def f(root):
            if not root:
                self.res.append(self.cur.copy())
                return None
            self.cur.append(root.val)
            l = f(root.left)
            r = f(root.right)
            self.cur.pop()
        f(root)
        ans = 0
        for r in self.res:
            cur = 1
            for i in range(1, len(r)):
                if r[i] == r[i - 1] + 1:
                    cur += 1
                else:
                    ans = max(ans, cur)
                    cur = 1
            ans = max(ans, cur)
        return ans 
