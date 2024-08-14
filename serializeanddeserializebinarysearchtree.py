
#Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

#Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

#The encoded string should be as compact as possible.

#exact same solution as serilaize and deserialize binary tree

#Example 1:

#Input: root = [2,1,3]
#Output: [2,1,3]
#Example 2:

#Input: root = []
#Output: []

#python3 solution:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def f(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val)) #append strings, not ints!
            f(root.left)
            f(root.right)


        f(root) #remember to call the recursion outside to start it
        return ",".join(res) #we need to seperate each node value with a comma
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        a = data.split(",") #converting back into a list based on the comma we used when we returned res above
        self.i = 0
        def f():
            if a[self.i] == "N": #base case
                self.i += 1
                return None #reached leaf 
            root = TreeNode(a[self.i]) 
            self.i += 1 #must always increment i to go to next value in our list!
            root.left = f()
            root.right = f()
            return root #must actually return the full tree itself at the end!
        return f()

