

#3157
#medium


#Given the root of a binary tree root where each node has a value, return the level of the tree that has the minimum sum of values among all the levels (in case of a tie, return the lowest level).

#Note that the root of the tree is at level 1 and the level of any other node is its distance from the root + 1.

 

#Example 1:

#Input: root = [50,6,2,30,80,7]

#Output: 2

#Explanation:

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        d = deque()
        d.append(root)
        res = []
        minsum = float('inf')
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
                minsum = min(minsum, sum(level))
        print(res)
        print(minsum)
        for i in range(len(res)):
            if sum(res[i]) == minsum:
                return i + 1
