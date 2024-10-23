
#1214
#medium

#Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.


#Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
#Output: true
#Explanation: 2 and 3 sum up to 5.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        first = []
        d = deque()
        d.append(root1)
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
        for i in range(len(res)):
            for j in range(len(res[i])):
                first.append(res[i][j])
        second = []
        d = deque()
        d.append(root2)
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
        for i in range(len(res)):
            for j in range(len(res[i])):
                second.append(res[i][j])
        print(first)
        print(second)
        for f in first:
            for s in second:
                if f + s == target:
                    return True
        return False
