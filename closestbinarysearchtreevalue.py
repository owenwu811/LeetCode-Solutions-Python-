#270
#easy

#Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.
#Input: root = [4,2,5,1,3], target = 3.714286
#Output: 4


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
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
        myheap = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                heapq.heappush(myheap, (abs(target - res[i][j]), res[i][j]))
        print(myheap)
        return myheap[0][1]
