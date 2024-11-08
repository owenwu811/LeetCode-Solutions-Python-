
#1022
#easy

#You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

#For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

#The test cases are generated so that the answer fits in a 32-bits integer.


#Input: root = [1,0,1,0,1,0,1]
#Output: 22
#Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.cur = [] 
        self.res = []
        def f(root):
            if not root:
                return None 
            self.cur.append(root.val)
            l = f(root.left)
            r = f(root.right)
            if not root.left and not root.right:
                print(self.cur)
                self.res.append(self.cur.copy())
            self.cur.pop()


        f(root)
        print(self.res)
        new = []
        for r in self.res:
            cur = ""
            for a in r:
                cur += str(a)
            print(cur)
            new.append(cur)
        print(new)
        tot = 0
        for n in new:
            print(int(n, 2))
            tot += int(n, 2)
        return tot
