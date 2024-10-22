#1612
#medium


#A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators. In this problem, we only consider the '+' operator (i.e. addition).

#You are given the roots of two binary expression trees, root1 and root2. Return true if the two binary expression trees are equivalent. Otherwise, return false.

#Two binary expression trees are equivalent if they evaluate to the same value regardless of what the variables are set to.

 

#Example 1:

#Input: root1 = [x], root2 = [x]
#Output: true


#my own solution using python3:

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        self.first = dict()
        def f(root1):
            if not root1:
                return None
            if root1.val not in self.first:
                self.first[root1.val] = 0
            self.first[root1.val] += 1
            l = f(root1.left)
            r = f(root1.right)
        f(root1)
        print(self.first)
        self.second = dict()
        def f(root2):
            if not root2:
                return None
            if root2.val not in self.second:
                self.second[root2.val] = 0
            self.second[root2.val] += 1
            l = f(root2.left)
            r = f(root2.right)
        f(root2)
        print(self.second)
        return self.first == self.second
