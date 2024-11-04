
#285
#medium

#Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

#The successor of a node p is the node with the smallest key greater than p.val.

#Input: root = [2,1,3], p = 1
#Output: 2
#Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
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
        tmp = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                tmp.append(res[i][j])
        tmp.sort()
        print(tmp)
        if p and p.val == max(tmp):
            return None
        key = float('inf')
        for t in tmp:
            if p and p.val == t:
                print(p.val, t)
                for t in tmp:
                    if t > p.val:
                        key = t
                        break
                #key = t + 1
                #print(key)
                #break
        #if key not in tmp:
        #    return None
        print(key)
        myd = deque()
        myd.append(root)
        ans = []
        while myd:
            ll = []
            for i in range(len(myd)):
                cur = myd.popleft()
                if cur:
                    if cur.val == key:
                        return cur
                    ll.append(cur.val)
                    myd.append(cur.left)
                    myd.append(cur.right)
            if ll:
                ans.append(ll)
