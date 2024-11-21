

#1506
#medium

#You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

#Return the root of the N-ary tree.

#Custom testing:

#An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the null value (see examples).

#Input: tree = [1,null,3,2,4,null,5,6]
#Output: [1,null,3,2,4,null,5,6]

#my own solution using python3:

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        orig = []
        d = defaultdict(list)
        for t in tree:
            orig.append(t.val)
            #print(t.val)
            for a in t.children:
                d[t.val].append(a.val)
        #print(d)
        print(orig)
        bank = []
        for k in d:
            for a in d[k]:
                bank.append(a)
        print(d)
        if not d:
            return Node(orig[0])
        possible = []
        for k in d:
            if k not in bank:
                possible.append(k)
        print(possible)
        if not possible:
            return None
        ans = possible[0]
        if not d and not possible:
            print('h')
            return Node(List[0])
        for t in tree:
            if t.val == ans:
                return t
            for a in t.children:
                if a.val == ans:
                    return a
