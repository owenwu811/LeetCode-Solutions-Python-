#47%acceptancerate
#medium

#You are given the root of a binary tree and a positive integer k.

#The level sum in the tree is the sum of the values of the nodes that are on the same level.

#Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

#Note that two nodes are on the same level if they have the same distance from the root.

#Input: root = [5,8,9,2,1,3,7,4,6], k = 2
#Output: 13
#Explanation: The level sums are the following:
#- Level 1: 5.
#- Level 2: 8 + 9 = 17.
#- Level 3: 2 + 1 + 3 + 7 = 13.
#- Level 4: 4 + 6 = 10.
#The 2nd largest level sum is 13.


#my own solution in python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d = deque()
        d.append(root)
        tmp = []
        while d:
            levelsum = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    levelsum.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if levelsum:
                tmp.append(sum(levelsum))
        myheap = []
        for t in tmp:
            heapq.heappush(myheap, -t)
        if len(tmp) < k: return -1
        res = 0
        while k > 0:
            res = -1 * heapq.heappop(myheap)
            k -= 1
        return res
