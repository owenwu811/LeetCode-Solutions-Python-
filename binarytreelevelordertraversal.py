


#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #return type is a list of lists
        res = []
        #we use a deque to keep track of when we have reached the bottom of the tree and no more children nodes from the current node exist
        d = deque()
        #we append the root, or the 1st value of the tree, not the entire list itself - 3 in the case of root = [3,9,20,null,null,15,7] is appended to the deque
        d.append(root)
        #while the deque is not empty
        while d:
            #represents all the nodes from left to right in order at each level in the tree 
            level = []
            #iterate through our deque using indexes
            for i in range(len(d)):
                #remove our root, or, 3, in our case, from our tree and set currentnode variable to 3
                currentnode = d.popleft()
                #3 is not none, so we append the value of the node - 3 - to the level list in order 
                if currentnode is not None:
                    level.append(currentnode.val)
                    #add the child nodes - only 2 of them in a binary tree at most - to the deque in order of left to right
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            #after we have iterated through the deque at a particular level - after i = 0, i = 0, 1, i = 0, 1, 2, 3 - the for loop dosen't count the child nodes we add to the deque. if our level sublist has nodes in it, append it to the final result lisst
            if level:
                res.append(level)
        #while loop terminates because we have hit the bottom of the tree and have no more child nodes to add to the deque 
        return res
