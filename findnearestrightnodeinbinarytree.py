
#1602

#medium


#Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.

#Input: root = [1,2,3,null,4,5,6], u = 4
#Output: 5
#Explanation: The nearest node on the same level to the right of node 4 is node 5.

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        d = deque()
        d.append(root)
        res = []
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    #print(d)
                    #if cur.val == u.val and d:
                    #    return d.popleft()
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                print(level)
                for i, l in enumerate(level):
                    print(l)
                    if l == u.val and i < len(level) - 1:
                        return TreeNode(level[i + 1])
                    if l == u.val and i == len(level) - 1:
                        return None
                res.append(level)
        print(res)
        
