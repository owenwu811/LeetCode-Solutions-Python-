
#easy 
#87%acceptancerate

#Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

#Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#Output: 32
#Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

#my own solution using python3:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        fres = []
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
                fres.append(level)


        for i in range(len(fres)):
            for j in range(len(fres[i])):
                if fres[i][j] >= low and fres[i][j] <= high:
                    self.res += fres[i][j]
        return self.res
