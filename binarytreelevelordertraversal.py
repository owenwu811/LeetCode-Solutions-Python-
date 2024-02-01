

#this problem is similar to binary tree right side view 

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



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = deque()
        #this will only happen once - to add the root node of the tree to the deque so that while q will even begin executing 
        q.append(root)
        while q:
            #len is taken before the for loop
            currentgeneration = len(q)
            #the level list just holds the integer values of all nodes in the current level 
            level = []
            #the for loop just represents the number of iterations in the current level of the tree using i 
            for i in range(currentgeneration):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    #children at down one level in the tree compared to the parent aka children are not at the same level as current node that we are evaluating now is at, and, if there are children in the current level, the while loop - while q - will become true after we append the current level - q only has something if we added children to it
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
            res = []
            #represents if we have anymore children and holds all the children at one level to be processed later
            d = deque()
            #we have to append the root node to kick off the while loop
            d.append(root)
            while d:
                #this just holds all the integer values of nodes at a current level of the tree
                level = []
                #this determines the number of iterations using i in each level of the tree
                currentgeneration = len(d)
                for i in range(currentgeneration):
                    currentnode = d.popleft()
                    if currentnode is not None:
                        #if our currentnode is not none, add it to the level list in order using append
                        level.append(currentnode.val)
                        #this will be used to determine if while d is true since children added here at one level down from the current node and will be evaluated - note that the currentgeneration (meaning current level of tree in intuitive way) that equals variable of len(d) is set statically before the for loop begins
                        d.append(currentnode.left)
                        d.append(currentnode.right)
                if level:
                    res.append(level)
            return res


#1/3/24 refresher:

res = []
d = deque()
d.append(root)
#there are child nodes that were added at the previous level meaning this level of the tree has nodes 
while d:
    #the values of the nodes in a particular level of the tree will be kept in this list
    level = []
    #how many iterations as indexes in the current level of the tree
    for i in range(len(d)):
        #from left to right direction in the current level of the tree, remove each node from the tree and set current generation equal to the value of that node
        currentgeneration = d.popleft()
        #we need to make sure that the value of the current node is not None
        if currentgeneration is not None:
            level.append(currentgeneration.val)
            #trees go from left to right - these are appending the children nodes from the perspective of the currentgeneration node we are on 
            d.append(currentgeneration.left)
            d.append(currentgeneration.right)
    if level:
        res.append(level)
return res

#notes:

#the line - while d - will mostly always be true on the 1st time it is called, but future times when it is recalled will depend on if children were added in the previous iterations from the new while loop call's perspective
#the level [] list represents the node values for the current level of the input tree
#the deque d() represents the nodes themselves for the current level of the input tree 
#the line - if level: res.append(level) - is necessary because we don't want empty sublists in the output - [[3], [9, 20], [15, 7]] instead of [[3], [9, 20], [15, 7], []]
#IMPORTANT: the level = [] list after the line - while d - GETS CLEARED EVERYTIME THE line - while d - is recalled after the execution of the line - res.append(level). The reason the level [] list gets cleared in this manner is because every new level of the input tree starts fresh - think children's generation vs parent's generation as levels in the tree. you aren't in your parent's generation. 
#we use the d.popleft() method to simulate the order of going from left to right in a particular level in the input tree - popping from left to right and adding to the level list from left to right (keeping the order depicted in the input tree)
       
#1/4/24 refresher solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we use a deque to keep track of the nodes at every level of the input tree
        d = deque()
        res = []
        #we need to start with the root node of the tree as that is the first level
        d.append(root)
        #while our deque has elements inside of it
        while len(d) > 0:
            #iterating through our deque
            #level list will represent all the values of the nodes at the current level of the tree
            level = []
            for index in range(len(d)):
                #we want to pop the values of the nodes from left to right and add those values to our level list as long as the node itself is not a null value
                currentnode = d.popleft()
                if currentnode is not None:
                    level.append(currentnode.val)
                    #we add the children nodes to the deque from the perspective of our current level so that the while loop can continue - the while loop continues as long as there is a child level. after the while loop continues for the next level, the level list is cleared 
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            #we do not want empty sublists in our result, so we must check that our level list has elements inside of it
            if len(level) > 0:
                res.append(level)
        #after we have gone through all levels meaning there is nothing in the current deque because there were no children added for the current level, we can return the res list of lists as the solution
        return res


#1/7/24 refresher solution - my own solution in python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #keep track of nodes at the current level in our input tree
        res = []
        d = deque()
        d.append(root)
        while len(d) > 0:
            #level is used to keep track of the integer values of the nodes at the current level in our input tree
            level = []
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    level.append(currentnode.val)
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if level:
                res.append(level)
        return res

#1/9/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        #deque is nodes at current level of input tree
        d = deque()
        d.append(root)
        #while there are children aka another level in the input tree we haven't covered yet, this while loop will iterate
        while d:
            #you don't clear the level at every iteration of the deque but only at each level of the input tree, so this level list goes above the for loop
            level = []
            for i in range(len(d)):
                #level is values at current level of input t
                #unpacking the deque's nodes from left to right
                currentnode = d.popleft()
                if currentnode is not None:
                    level.append(currentnode.val)
                    #add children
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            #no empty lists in the output
            if level:
                res.append(level)
        return res


#1/14/24 refresher practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        #nodes at each level of input tree
        d = deque()
        d.append(root)
        while len(d) > 0:
            #level gets cleared after traversing all nodes at a particular level of the input tree, so after the for loop finishes for a particular level of the input tree, we see if d still has elements aka there is another level in the input tree, and if there is, then we start with an empty list as level as we haven't added and node values to the level list yet 
            level = []
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    level.append(currentnode.val)
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if level:
                res.append(level)
        return res

#1/19/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #our deque will store all the nodes at the current level of the input tree
        d = deque()
        res = []
        #the first level of our input tree only contains the root, so we append only the root node of the tree to our deque list
        d.append(root)
        #this while loop will terminate when there are no more levels aka children from the perspective of the previous level
        while len(d) > 0:
            level = []
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    level.append(currentnode.val)
                    #adding the children
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if level:
                res.append(level)
        return res


#1/25/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we want to return each value of each node of each level of the tree from left to right and from the top level down to the bottom level
        #our deque will keep track of the nodes at each level of the input tree
        res = []
        d = deque()
        #our first level
        d.append(root)
        #we still haven't traversed all levels yet
        while d:
            #holds all the values of each node at each level of the input tree
            level = []
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    level.append(currentnode.val)
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            #we don't want empty arrays in our output result
            if level:
                res.append(level)
        return res

#1/28/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            #deque will contain all nodes at a particular level of the input tree
            d = deque()
            res = []
            #our first level has only one node 
            d.append(root)
            #meaning we have another level in the input tree that we haven't processed yet
            while len(d) > 0:
                #since we know we have another level in our input tree that hasn't yet been processed, we need to empty our level list to make sure our level list contains only values of the nodes from left to right at the current level of our input tree
                level = []
                #each iteration or node in the level
                for i in range(len(d)):
                    #we are popping the current level's nodes off from left to right, one by one
                    currentnode = d.popleft()
                    if currentnode is not None:
                        level.append(currentnode.val)
                        #after we popped all nodes off from left to right at current level, we still need to add the children (level below) from left to right as well
                        d.append(currentnode.left)
                        d.append(currentnode.right)
                #a current level has ended, so we need to determine if our level has elements in it and isn't an empty list since the output sample dosen't ask us for empty lists representing null values
                if level:
                    res.append(level)
            return res
                
#2/1/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #will store all nodes at a current level of the bst
        d = deque()
        d.append(root)
        res = []
        while d:
            #clear our list to make room the exactly the nodes in this new level we are about to traverse
            level = []
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    level.append(currentnode.val)
                    #adding children
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if len(level) > 0:
                res.append(level)
        return res
