#302
#hard

#You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

#The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

#Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

#You must write an algorithm with less than O(mn) runtime complexity

#Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
#Output: 6


#my own solution using python3:

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        r, c = [], []
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == "1":
                    r.append(i)
                    c.append(j)
        print(r, c)
        x, y = max(r) - min(r) + 1, max(c) - min(c) + 1
        return x * y
