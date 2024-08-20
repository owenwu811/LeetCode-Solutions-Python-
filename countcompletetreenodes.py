
#Given the root of a complete binary tree, return the number of the nodes in the tree.

#According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

#Design an algorithm that runs in less than O(n) time complexity.

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        d = deque()
        d.append(root)
        res = 0
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    res += 1
                    d.append(cur.left)
                    d.append(cur.right)
        return res
