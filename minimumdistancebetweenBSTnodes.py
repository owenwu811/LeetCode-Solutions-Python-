
#783
#easy

#Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

#Input: root = [4,2,6,1,3]
#Output: 1

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
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
        print(res)
        tmp = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                tmp.append(res[i][j])
        tmp.sort()
        res = float('inf')
        for i in range(1, len(tmp)):
            res = min(res, abs(tmp[i] - tmp[i - 1]))
        return res
