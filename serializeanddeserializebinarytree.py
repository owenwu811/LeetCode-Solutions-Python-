#Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

#Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

#Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



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
        vals = data.split(",") #turns string input back into a list with comma split
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
