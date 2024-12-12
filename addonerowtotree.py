
#623
#medium

#Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

#Note that the root node is at depth 1.

#The adding rule is:

#Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
#cur's original left subtree should be the left subtree of the new left subtree root.
#cur's original right subtree should be the right subtree of the new right subtree root.
#If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.


#my own solution using python3:

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        d = deque()
        d.append([root, 1])
        if depth == 1:
            newroot = TreeNode(val)
            newroot.left = root
            newroot.right = None  
            return newroot
        while d:
            for i in range(len(d)):
                cur, curd = d.popleft() 
                if cur:
                    print(cur.val, curd)
                    if cur.left:
                        print(cur.left.val)
                    if curd == depth - 1:
                        origleft = cur.left
                        origright = cur.right
                        cur.left = TreeNode(val)
                        cur.right = TreeNode(val)
                        cur.left.left = origleft
                        cur.right.right = origright
                    d.append([cur.left, curd + 1])
                    d.append([cur.right, curd + 1])
        return root
