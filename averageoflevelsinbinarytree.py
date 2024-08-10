#Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

#Input: root = [3,9,20,null,null,15,7]
#Output: [3.00000,14.50000,11.00000]
#Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
#Hence return [3, 14.5, 11].

#my own solution in python3:


#again, the same idea with level order traversal:



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        d = deque()
        d.append(root)
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                res.append(sum(level) / len(level))
        
        return res
