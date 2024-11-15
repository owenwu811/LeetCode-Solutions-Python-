

#988
#medium

#You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

#Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

#As a reminder, any shorter prefix of a string is lexicographically smaller.

#For example, "ab" is lexicographically smaller than "aba".
#A leaf of a node is a node that has no children.

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        self.stack = []
        self.res = []
        def f(root):
            if not root:
                return None
            self.stack.append(root.val)
            l = f(root.left)
            r = f(root.right)
            if not root.left and not root.right:
                print(self.stack)
                self.res.append(self.stack.copy())
            self.stack.pop()
        f(root)
        print(self.res)
        print(letters)
        possible = []
        for r in self.res:
            tmp = ""
            for i in range(len(r)):
                tmp += letters[r[i]]
            tmp = tmp[::-1]
            print(tmp)
            possible.append(tmp)
        possible.sort()
        return possible[0]
