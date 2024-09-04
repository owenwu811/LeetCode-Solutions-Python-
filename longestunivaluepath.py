#Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

#The length of the path between two nodes is represented by the number of edges between them.


#687

#correct python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root, parent):
            if not root:
                return 0
            l = dfs(root.left, root)
            r = dfs(root.right, root)
            self.ans = max(self.ans, l + r)
            if root and parent and root.val == parent.val:
                return max(l, r) + 1
            return 0
        dfs(root, None)
        return self.ans
