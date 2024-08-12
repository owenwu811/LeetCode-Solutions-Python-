


#python3 solution (missed this question):


Construct binary search tree from preorder traversal:

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

      8
   5    10
1  7      12


class Solution:
   def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
       if not preorder:
           return None
       root = TreeNode(preorder[0])
       i = 1
       while i<len(preorder) and  preorder[i] < root.val:
           i+=1
       root.left = self.bstFromPreorder(preorder[1:i])
       root.right = self.bstFromPreorder(preorder[i:])
       return root


#i will land on 4 because preorder[4] = 10, and 10 is not smaller than 8
#and then root.left will be preorder[1:4], which is 5, 1, 7 aka the left subtree
#and then now root = TreeNode(preorder[0]) becomes 5
#i = 1
#remember that preorder is now [5, 1, 7] and not the entire input [8,5,1,7,10,12]
#while 1 < len(preorder) and preorder[1] < root.val (1 < 5) > True, so increment i
#i = 2
#2 < len(preorder) and preorder[2] < root.val (7 < 5) > False
#root.left = preorder[1:2] from [5, 1, 7]
#so now preorder = [1] and not the entire input [8,5,1,7,10,12]
#root = TreeNode(1)
#while 1 < len(preorder) and preorder[1] < root.val: (False)
#root.left = preorder[1:1] > so now preorder is an empty list
#now, if not preorder evaluates to True, so we return None
#we backtrack so that preorder gets back to one level above [1]
#root.right = preorder[1:] > so now preorder is also an empty list
#if not preorder evaluates to True, so we return None
#so now our return value is [1] - line return root executes
#now, we backtrack and preorder becomes [5, 1, 7], and we call root.right = preorder[i:]
#so now root.right yields a list of just [7]
#root = 7
#i = 1
#while 1 < len(preorder) and 7 < 7 (false):
#root.left = preorder[1:1] > empty list
#if not preorder - True, so we return None
#root.right = preorder[1:] > empty list
#if not preorder - True, so we return None
#return root (return 7) since we hit our leaf node
#backtrack to root.right, which is [10, 12]
#root = 10
#i = 1
#while 1 < len(preorder) and 12 < 10 (false):
#now we call root.left (10s left is None)
#if not preorder is True, so return None
#
