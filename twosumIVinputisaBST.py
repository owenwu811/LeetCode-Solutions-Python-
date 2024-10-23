
#653
#easy


#Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
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
        tmp = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                tmp.append(res[i][j])
        print(tmp)
        tmp.sort()
        print(tmp)
        l, r = 0, len(tmp) - 1
        while l < r:
            if tmp[l] + tmp[r] == k:
                return True
            elif tmp[l] + tmp[r] > k:
                r -= 1
            else:
                l += 1
        return False
