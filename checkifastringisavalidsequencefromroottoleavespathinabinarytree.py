
#1430
#medium

#Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

#We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.


#Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
#Output: true
#Explanation: 
#The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
#Other valid sequences are: 
#0 -> 1 -> 1 -> 0 
#0 -> 0 -> 0


#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        self.arr = arr
        self.cur = []
        self.res = False
        def f(root):
            if not root:
                return None
            self.cur.append(root.val)
            if not root.left and not root.right:
                print(self.cur)
                if self.cur == self.arr:
                    self.res = True
                
            l = f(root.left)
            r = f(root.right)
            self.cur.pop()
        
        f(root)
        return self.res
