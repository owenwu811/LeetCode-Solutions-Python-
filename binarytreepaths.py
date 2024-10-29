
#257
#easy

#Given the root of a binary tree, return all root-to-leaf paths in any order.

#A leaf is a node with no children.

#Input: root = [1,2,3,null,5]
#Output: ["1->2->5","1->3"]

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.cur = []
        def f(root):
            if not root:
                return None
            self.cur.append(root.val)
            #print(self.cur)
            if not root.left and not root.right:
                print(self.cur)
                new = ""
                for i, c in enumerate(self.cur):
                    new += str(c)
                    if i < len(self.cur) - 1:
                        new += "-"
                        new += ">"
                self.res.append(new)
            l = f(root.left)
            r = f(root.right)
            self.cur.pop()
            return root
        f(root)
        print(self.res)
        return self.res
