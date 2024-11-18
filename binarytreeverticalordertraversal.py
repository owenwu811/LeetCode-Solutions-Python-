
#314
#medium

#Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

#If two nodes are in the same row and column, the order should be from left to right.

#Input: root = [3,9,20,null,null,15,7]
#Output: [[9],[3,15],[20],[7]]

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()
        d.append([root, 1])
        res = []
        while d:
            level = []
            for i in range(len(d)):
                cur, pos = d.popleft()
                if cur:
                    level.append([cur.val, pos])
                    d.append([cur.left, pos - 1])
                    d.append([cur.right, pos + 1])
            if level:
                res.append(level)
        print(res)
        d = defaultdict(list)
        for r in res:
            #print(r)
            for a in r:
                print(a)
                d[a[1]].append(a[0])
        print(d)
        sortedd = dict(sorted(d.items(), key=lambda x: x[0]))
        print(sortedd)
        ans = []
        for s in sortedd:
            ans.append(sortedd[s])
        return ans
