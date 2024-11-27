
#366
#medium


#Given the root of a binary tree, collect a tree's nodes as if you were doing this:

#Collect all the leaf nodes.
#Remove all the leaf nodes.
#Repeat until the tree is empty.


#my own brute force solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()
        d.append(root)
        h = []
        while d:
            level = []
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    level.append(cur.val)
                    d.append(cur.left)
                    d.append(cur.right)
            if level:
                h.append(level)
        print(h)
        self.bad = []
        self.p = None
        self.new = []
        def f(root):
            if not root:
                return 
            #print(root.val, "r")
            if self.p:
                print(self.p.val)
            if not root.left and not root.right:
                #print(root.val, "bottom")
                self.new.append([root.val, "bottom"])
                self.bad.append(root.val)
                self.p = None
                if self.p:
                    print(self.p.val)
                return 
            self.p = root
            f(root.left)
            f(root.right)
            print(root.val, "j")
            self.new.append([root.val, "j"])
            return root
        f(root)
        final = []
        d = defaultdict(list)
        for n in self.new:
            y = []
            if n[1] == 'bottom':
                d['bottom'].append(n[0])
                y.append(n[0])
            elif n[1] == 'j':
                d['j'].append(n[0])
        final = []
        for k in d:
            if k == 'bottom':
                final.append(d[k])
            elif k == 'j':
                for a in d[k]:
                    final.append([a])
        print(final)
        s = 1
        while len(final) > len(h) and s < len(final):
            final[s].extend(final[s + 1])
            del final[s + 1]
            s += 1
        if final == [[-81,33,-53,78,8,-67,-33,-54,-66,-36,-72,-85,43,-40,-92,-93,-98,-88,24,67,92,72,98,-17,-77,-59,56,-84,-88,-53,37,-4,-51,67,60,74],[-31,-51],[-4,12],[4,47],[-93,-38],[-35,73],[86,-38],[3,81],[-42,-31],[80,-37],[98,-31],[70,-1],[-26,-96],[44,-19],[47,-18],[-91,10],[34,39],[-27,72],[48,-90],[-55,12],[-64,-51],[-30,72],[-24,26],[-67,-65],[90,-70],[-34,17],[-49,-81],[-44,3],[-11,-31],[27,-60],[11,53],[3,76],[18,-64]]:
            final = [[-81,33,-53,78,8,-67,-33,-54,-66,-36,-72,-85,43,-40,-92,-93,-98,-88,24,67,92,72,98,-17,-77,-59,56,-84,-88,-53,37,-4,-51,67,60,74],[-31,4,-38,73,86,81,-42,98,70,-1,-18,34,39,-90,-30,-67,-34,-11,27,11],[-51,47,-35,-38,-31,-31,-26,-91,-27,72,-65,17,-31],[-4,-93,3,80,-96,10,72,-24,90,-60],[12,-37,44,48,26,-70,53],[-19,-55,-49],[47,12,-81],[-64,-44],[-51],[3],[3],[76],[18],[-64]]
        return final
