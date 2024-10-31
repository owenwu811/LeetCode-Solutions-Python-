
#531
#medium


#Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

#A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

#Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
#Output: 3
#Explanation: All the three 'B's are black lonely pixels.


#my own solution using python3:

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        tmp = []
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] == "B":
                    tmp.append([i, j])
        print(tmp)
        rows, cols = [], []
        for t in tmp:
            rows.append(t[0])
            cols.append(t[1])
        print(rows, cols)
        res = 0
        for t in tmp:
            if rows.count(t[0]) == 1 and cols.count(t[1]) == 1:
                res += 1
        return res
