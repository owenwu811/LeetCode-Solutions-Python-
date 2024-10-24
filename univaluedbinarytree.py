
#965
#easy

#A binary tree is uni-valued if every node in the tree has the same value.

#Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.



#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
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
        new = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                new.append(res[i][j])
        return len(set(new)) == 1
