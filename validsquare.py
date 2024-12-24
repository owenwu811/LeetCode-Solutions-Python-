#593
#medium

#Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

#The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

#A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

#Example 1:

#Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
#Output: true
#Example 2:

#Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
#Output: false
#Example 3:

#Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
#Output: true


#my own solution using python3:

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        x, y = [], []
        if p1[0] == p1[1] and p2[0] == p2[1] and p3[0] != p3[1] and p2[0] != p3[0] and p2[1] != p3[1]:
            return False
        if p1 == p2 and p3 != p1 or p2 == p4 and p2 != p3:
            return False
        if p1 == p2 == p3 or p2 == p3 == p4:
            return False
        if p1 == p3 and p2 == p4:
            return False
        x.append(p1[0])
        x.append(p2[0])
        x.append(p3[0])
        x.append(p4[0])
        x.sort()
        print(x)
        y.append(p1[1])
        y.append(p2[1])
        y.append(p3[1])
        y.append(p4[1])
        y.sort()
        print(y)
        tot = x + y
        print(tot)
        for i, t in enumerate(tot):
            tot[i] = abs(t)
        if len(set(tot)) == 1 and math.prod(tot) > 0:
            return True
        zeroc, otherc = 0, 0
        for t in tot:
            if t == 0:
                zeroc += 1
            else:
                otherc += 1
        ratios = []
        if p1[0] == p1[1] and p2[0] != p2[1] or p3[0] == p3[1] and p4[0] != p4[1]:
            return False
        for i, c in enumerate(x):
            ratios.append(abs(c - y[i]))
        print(zeroc, otherc)
        return len(set(ratios)) == 1 and zeroc <= otherc
        
