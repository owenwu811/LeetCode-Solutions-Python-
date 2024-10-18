

#501
#easy


#Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

#If the tree has more than one mode, return them in any order.

#Assume a BST is defined as follows:

#The left subtree of a node contains only nodes with keys less than or equal to the node's key.
#The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
#Both the left and right subtrees must also be binary search trees.



#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
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
        new = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                new.append(res[i][j])
        md = dict()
        for r in new:
            if r not in md:
                md[r] = 0
            md[r] += 1
        target = max(md.values())
        ans = []
        for k in md:
            if md[k] == target:
                ans.append(k)
        return ans
