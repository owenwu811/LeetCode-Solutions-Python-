
#1222
#medium

#On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one white king.

#You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni] represents the position of the ith black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king.

#Return the coordinates of the black queens that can directly attack the king. You may return the answer in any order.

#Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
#Output: [[2,2],[3,4],[4,4]]


#my own solution using python3:

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        kx, ky = king[0], king[1]
        #[3, 3]
        #[3, 0]
        d = defaultdict(list)
        for x, y in queens:
            if x < kx and y == ky:
                #[2, 2]
                #[0, 2]
                d["above"].append([x, y])
                d["above"].sort(key=lambda x: x[0], reverse=True)
            if x > kx and y == ky:
                #[3, 4]
                #[4, 4] or [5, 4]
                d["below"].append([x, y])
                d["below"].sort(key=lambda x: x[0])
            if x == kx and y < ky:
                #[2, 2]
                #[2, 1] or [2, 0]
                d["left"].append([x, y])
                d["left"].sort(key=lambda x: x[1], reverse=True)
            if x == kx and y > ky:
                #[2, 2]
                #[2, 3] or [2, 4]
                d["right"].append([x, y])
                d["right"].sort(key=lambda x: x[1])
            if x > kx and y > ky:
                if x - kx == y - ky:
                    #[1, 2]
                    #[2, 3] or [3, 4]
                    heapq.heappush(d["pp"], (x - kx + y - ky, [x, y]))
                    #d["pp"].append([x, y])
            if x < kx and y < ky:
                if kx - x == ky - y:
                    #[2, 3]
                    #[0, 1] or [1, 2]
                    heapq.heappush(d["nn"], (kx - x + ky - y, [x, y]))
                    #d["nn"].append([x, y])
            # K        Q
            #[1, 2] > [0, 3]
            if kx > x and ky < y:
                if kx - x == y - ky:
                    #[2, 4]
                    #[1, 5] or [0, 6]
                    heapq.heappush(d["ur"], (kx - x + y - ky, [x, y]))
                    #d["ur"].append([x, y])
            #KX  KY    QX
            #[1, 2]   [3, 0]
            if kx < x and ky > y:
                if x - kx == ky - y:
                    #[1, 2]
                    #[2, 1] or [3, 0]
                    heapq.heappush(d["dl"], (x - kx + ky - y, [x, y]))
                    #d["dl"].append([x, y])
        print(d)
        ans = []
        for keys in d:
            first = d[keys][0]
            if type(first) == tuple:
                print(first[-1])
                ans.append(first[-1])
            else:
                print(first)
                ans.append(first)
        return ans
            
            
