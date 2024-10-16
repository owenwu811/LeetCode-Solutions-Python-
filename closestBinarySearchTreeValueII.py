#272
#Hard


#Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

#You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

#Input: root = [4,2,5,1,3], target = 3.714286, k = 2
#Output: [4,3]


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        d = deque()
        d.append(root)
        res = []
        while d:
            level  = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                res.append(level)
        print(res)
        tmp = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                tmp.append(res[i][j])
        print(tmp)
        myheap = []
        res = float('inf')
        for t in tmp:
            cur = abs(target - t)
            print(cur)
            heapq.heappush(myheap, [cur, t])
        myheap.sort(key=lambda x: x[0])
        print(myheap)
        actual = []
        for i in range(k):
            actual.append(myheap[i][1])
        return actual
