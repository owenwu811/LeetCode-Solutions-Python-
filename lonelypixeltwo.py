#533
#medium

#Given an m x n picture consisting of black 'B' and white 'W' pixels and an integer target, return the number of black lonely pixels.

#A black lonely pixel is a character 'B' that located at a specific position (r, c) where:

#Row r and column c both contain exactly target black pixels.
#For all rows that have a black pixel at column c, they should be exactly the same as row r.

#Input: picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3
#Output: 6
#Explanation: All the green 'B' are the black pixels we need (all 'B's at column 1 and 3).
#Take 'B' at row r = 0 and column c = 1 as an example:
# - Rule 1, row r = 0 and column c = 1 both have exactly target = 3 black pixels. 
# - Rule 2, the rows have black pixel at column c = 1 are row 0, row 1 and row 2. They are exactly the same as row r = 0.

#my own solution using python3:

class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        cols, rows = [], []
        cnt = 0
        tot = 0
        myflag = False
        for p in picture:
            if "W" in p:
                myflag = True
            tot += p.count("B")
            if p.count("B") != target:
                cnt += 1
            rows.append(p)
        if not myflag:
            return target * target
        if cnt == len(picture):
            return 0
        if tot == target:
            return target
        i = 0
        while i < len(picture[0]):
            curcol = []
            for j in range(len(picture)):
                curcol.append(picture[j][i])
            i += 1
            cols.append(curcol)
        res = 0
        for i, c in enumerate(cols):
            current = []
            if c.count("B") == target:
                for j in range(len(c)):
                    if c[j] == "B":
                        current.append(j)
                rowc = []
                for item in current:
                    rowc.append(rows[item])
                flag = True  
                for a in range(len(rowc)):
                    for b in range(a + 1, len(rowc)):
                        if rowc[a] != rowc[b] or rowc[a].count("B") != target or rowc[b].count("B") != target:
                            flag = False  
                            break
                if flag: 
                    res += target
                    
        return res
       
