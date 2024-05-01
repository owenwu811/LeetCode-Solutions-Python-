#Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

#Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

#Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


#DFS PREORDER TRAVERSAL WAY:

#python3 solution:

class Codec:
    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N") #remember that our list has [3, "N", "N"] with the N's signaling the leaf nodes of the tree, so we can backtrack 
                return
            res.append(str(root.val)) #just think we have a TreeNode with .val attribute. turn it into a string by type casting into string with str() and then append to result list
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res)
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",") #turns string input back into a list with comma split. you know data is an input str as stated in the method parameter
        self.i = 0
        def dfs():
            if vals[self.i] == "N": #we already know this node's value, so we can increment i
                self.i += 1 
                return None
            node = TreeNode(vals[self.i]) 
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

#practice again:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res) #returns a string - "1, 2, N, N, 3, 4, N, N, 5, N, N"
        
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",") #vals becomes a list from the last return in serialize - ["1", "2", "N", "N", "3", "4", "N", "N", "5", "N", "N"] - REMEMBER THAT WE ONLY HAVE INTEGER STRINGS LIKE 3 OR N STRINGS IN OUR LIST BECAUSE N WAS OUR SPECIAL CHARACTER AND WE ONLY PUT THOSE TWO TYPES IN OUR LIST!
        self.i = 0
        def dfs():
            if vals[self.i] == "N": #base case because vals is a list, so we can index into it with i to create our binary tree
                self.i += 1 #we see a None, so we increment i to go to the next character in our list to the right so i can index into it in the future
                return None #N special character in our list of strings stands for None as a TreeNode
            node = TreeNode(vals[self.i]) #becomes a TreeNode because we saw a non "N" in our list with vals[self.i]
            self.i += 1 #we always have to keep going to the next element in our list whether we see a number or a "N" in our list
            node.left = dfs() #dig down left because this is preorder dfs
            node.right = dfs() #even when building right, dig left first because this is preorder dfs
            return node #backtrack after we return, and we have to return the node we created
        return dfs() #kickoff start of recursive call 
        
       
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


#important notes:

#vals = ["1", "2", "N", "N", "3", "4", "N", "N", "5", "N", "N"] - 2 N N - means finished seperate completed subtree, so 3 is the right child node of 1. 
#i starts by pointing to 1, and since this is preorder dfs, we dig left from 1 node to 3 node to 4 node even though we are on 3 right subtree of 1. This is why node.left = dfs() line comes before node.right = dfs() - because preorder dfs means digging NLR. 
#NN means base case because we can't continue - we are on empty node 
#["1", "2", "N", "3"] - 3 is the right child of 2 while N is the left child of 2.

#when we create the node 1 with - node = TreeNode(vals[self.i]) - the computer reads the val = 1, left = None, and right = None, so the left and right attributes are set to None as default before we traverse down the tree to give 1 a left child!
#seeing a "N" in the vals list after indexing into the vals list with vals[self.i] means we still increment i to move to the next (right) elements in our vals list, and "N" corresponds to None when actually creating the TreeNode to signal empty bottom 
#after doing 2's right child as None with node.right = dfs() recursive call, we execute the return node line before backtracking back to node.right = dfs() to do 1's right child of node 3!

#4/15/24 practice:

class Codec:
    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res) #a string
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",") #a list of strings
        self.i = 0 #we need to index into the vals list
        def f():
            if vals[self.i] == "N": #we only have either integer strings or "N" strings in our vals list
                self.i += 1 #need to go to next element to right 
                return None #N corresponds to creating a None node
            node = TreeNode(vals[self.i]) #not "N", so we are seeing a "3", so create a 3 treenode object
            self.i += 1 #after we create either an integer or None, we need to go to next element to right so we can say after we do the next left recursion we actually have the element to the right of previous in the list and don't do infinite recursion
            node.left = f() #preorder DFS, so left first
            node.right = f() 
            return node 

#4/15/24:

class Codec:

    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res)
        
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",") #string.split(",") turns the string into an array!
        self.i = 0
        def f():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        return f()

#4/16/24:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res)
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",")
        self.i = 0
        def f():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        return f()


#4/17/24:

class Codec:

    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N") #[1, 2, 3, N, N, 4, 5]
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res)
        
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",")
        self.i = 0
        def f():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        return f()

#4/18/24 practice:

class Codec:

    def serialize(self, root): # Serialize the binary tree into a string
        arr = [] #store results in an array first. traverse tree preorder dfs way
        def f(root): 
            if root == None:
                arr.append("N")
                return #we reached bottom empty node of tree, so backtrack
            arr.append(str(root.val)) 
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(arr) #turn array back into string with comma seperator so we know how to differentiate nodes
        
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        #turn string back into array with the commas
        vals = data.split(",")
        self.i = 0 #we need to index into our new array
        def f():
            if vals[self.i] == "N": #N was our special character
                self.i += 1 #prevent infinite recursion by moving index pointer one to right (always do this wheter we see N or 3)
                return None #N corresponds to creating aka returning a None node
            node = TreeNode(vals[self.i]) #create a TreeNode object out of the "3" in our array
            self.i += 1 #prevents infinite recursion
            node.left = f() #preorder dfs to create other nodes in correct position relative to node we created above
            node.right = f() 
            return node #actually return the entire tree we created
        return f() #kickoff recursion - recursion returns an entire tree at end
        
#4/19/24:

class Codec:

    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res)

    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",")
        self.i = 0
        def f():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            node.left = f()
            node.right = f()
            return node
        return f()


#4/22/24:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res)
    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",")
        self.i = 0
        def f():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        return f()

#4/24/24:

class Codec:

    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            left = f(root.left)
            right = f(root.right)
        f(root)
        return ",".join(res)

    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",")
        self.i = 0
        def f():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        return f()

#4/30/24:

class Codec:

    def serialize(self, root): # Serialize the binary tree into a string
        res = []
        def f(root):
            if root == None:
                res.append("N")
                return
            res.append(str(root.val))
            f(root.left)
            f(root.right)
        f(root)
        return ",".join(res) #string


    def deserialize(self, data: str):  # Deserialize the string into a binary tree
        vals = data.split(",") #array
        self.i = 0
        def f():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        return f()

