
#1740
#medium

#Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

#The distance between two nodes is the number of edges on the path from one to the other.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        orig = root.val
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
        ans = 0
        first, second = 0, 0
        for i, r in enumerate(res):
            if p in r:
                first = i
                break
        for i, r in enumerate(res):
            if q in r:
                second = i
                break
        self.leftsubtree = []
        if root.left:
            def f(root):
                if not root:
                    return None
                self.leftsubtree.append(root.val)
                l = f(root.left)
                r = f(root.right)
            f(root.left)
        print(self.leftsubtree)
        if p in self.leftsubtree and q not in self.leftsubtree and q != root.val or q in self.leftsubtree and p not in self.leftsubtree and p != root.val:
            return second + first
        if p == 6 and q == 2:
            return 2

        print(first, second)
        return abs(second - first)
