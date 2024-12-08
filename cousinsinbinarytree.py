

#993
#easy

#Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

#Two nodes of a binary tree are cousins if they have the same depth with different parents.

#Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        myd = defaultdict(list)
        def f(root):
            if not root:
                return
            if root.left:
                myd[root.left.val].append(root.val)
            if root.right:
                myd[root.right.val].append(root.val)
            
            f(root.left) 
            f(root.right)
            

        f(root)
        print(myd)
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
                print(level)
                if x in level and y in level:
                    print(myd[x], myd[y])
                    if myd[x] != myd[y]:
                        return True  
        return False
