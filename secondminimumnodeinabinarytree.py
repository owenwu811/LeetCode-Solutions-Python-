
#671
#easy
#44.8% acceptance rate


#Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

#Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

#If no such second minimum value exists, output -1 instead.

#my own solution using python3:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
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
        myset = set()
        for i in range(len(res)):
            for j in range(len(res[i])):
                myset.add(res[i][j])
        new = []
        for s in myset:
            new.append(s)
        print(new)
        new.sort()
        if len(new) <= 1:
            return -1
        return new[1]
