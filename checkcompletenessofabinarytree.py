#958
#medium

#Given the root of a binary tree, determine if it is a complete binary tree.

#In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

#Input: root = [1,2,3,4,5,6]
#Output: true
#Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
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
                else:
                    level.append(None)
            if level:
                res.append(level)
        print(res)
        for idx, r in enumerate(res):
            if len(r) >= 2 and idx >= 1:
                if r[0] != None and r[1] == None and res[idx - 1][-1] == None:
                    return False
                if None not in r and res[idx - 1][-1] == None:
                    return False
                if r[0] != None and res[idx - 1][-1] == None:
                    return False
            for i, a in enumerate(r):
                if a == None: 
                    if i != len(r) - 1 and len(set(r)) != 1:
                        for j in range(i + 1, len(r)):
                            if r[j] != None:
                                return False
                elif a != None:
                    if i != len(r) - 1 and len(set(r)) != 1:
                        for j in range(i + 1, len(r)):
                            print(r[j])
        #[[1], [2, 3], [4, 5, 6, 7], 
        #[8, 9, 10, 11, 12, 13, None, None], 
        #[15, None, None, None, None, None, None, None, None, None, None, None], 
        #[None, None]]
        return True
