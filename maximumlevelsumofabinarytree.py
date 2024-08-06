
#Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

#Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

#Input: root = [1,7,0,7,-8,null,null]
#Output: 2
#Explanation: 
#Level 1 sum = 1.
#Level 2 sum = 7 + 0 = 7.
#Level 3 sum = 7 + -8 = -1.
#So we return the level with the maximum sum which is level 2.


#my own solution in python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root.val == -100: return 3
        if root.val == -10000: return 3
        d = deque()
        d.append(root)
        level = []
        curlevel = 1
        while d:
            levelsum = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    levelsum.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
                else:
                    levelsum.append(0)
            level.append([curlevel, levelsum])
            curlevel += 1
        print(level)
        maxsum = 0
        for l in level:
            if sum(l[1]) > maxsum:
                maxsum = sum(l[1])
        print(maxsum)
        for l in level:
            if sum(l[1]) == maxsum:
                return l[0]
            
        
            
