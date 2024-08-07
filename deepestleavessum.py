
#Given the root of a binary tree, return the sum of values of its deepest leaves.

#Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
#Output: 15


#my own solution in python3:

#we just want to take the sum of the last level, and each level's node values are in a sublist in res, so jut sum the last sublist in res as the anwser 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
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
        return sum(res[-1])
