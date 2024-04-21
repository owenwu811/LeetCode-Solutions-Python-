#An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

#You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

#To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

#Return the modified image after performing the flood fill.

 

#Example 1:


#Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]
#Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
#Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
#Example 2:

#Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
#Output: [[0,0,0],[0,0,0]]
#Explanation: The starting pixel is already colored 0, so no changes are made to the image.


#this is a recursion problem


#Solution: 
#At the beginning, we want to find the starting square and replace that square's value with color as given by the variable in the problem
# What we want to do is essentially check that every square to the left right up or down is the same value as the starting square provided by image[sr][sc], and if it is, stop recursing, and if it's not, then replace that square with the value of color
# In other words, we keep recursing to the left right up down until the new square we are stepping onto is already the same color, and if it's the same color, we step back by coming back from the direction we came in
#at the end, we return the new image once the recursion stops and the base case is reached 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #ensures we stop flooding if the square to the left, right, up, or down is already the same number aka already flooded
        if image[sr][sc] == color:
            return image

        starting = image[sr][sc]
        # Call the fill function using the class name Solution

        self.fill(image, sr, sc, starting, color)      
        #return image only occurs when we terminate the base case aka the base case becomes true and we stop recursion
        return image
    # Add the self parameter to the fill function to make it a method of the Solution class
    def fill(self, image, row, col, original_color, color):
        #we have two conditions: don't go out of bounds in up down right left of grid and don't step onto a square that already has the same value
        #these are boundary checks
        
        #if the pixel is out of bounds, return the grid and exit the problem. We don't do any more processing. 
        if (row < 0 or row >= len(image)) or (col < 0 or col >= len(image[0])):
            return 
        
        if image[row][col] != original_color: 
            return
        
        image[row][col] = color

        # Recursively fill the neighboring pixels in the four cardinal directions
        # when you move to the next row, that automatically implies down, and when you move to the next column, that automatically implies right
        self.fill(image, row + 1, col, original_color, color)  # Down
        self.fill(image, row - 1, col, original_color, color)  # Up
        self.fill(image, row, col + 1, original_color, color)  # Right
        self.fill(image, row, col - 1, original_color, color)  # Left

#my solution python3: - 12/24/23

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        self.fill(image, sr, sc, starting, color)
        return image
    def fill(self, image, sr, sc, starting, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != starting:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, starting, color)
        self.fill(image, sr - 1, sc, starting, color)
        self.fill(image, sr, sc + 1, starting, color)
        self.fill(image, sr, sc - 1, starting, color)


#my solution - python3 12/25/23:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color: # if the starting pixel is already equal to color, then there's nothing to fill
            return image
        self.fill(starting, sr, sc, color, image)
        return image
    def fill(self, starting, sr, sc, color, image):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color #we must set the 1 to 2 color so we don't revisit it
        self.fill(starting, sr + 1, sc, color, image)
        self.fill(starting, sr - 1, sc, color, image)
        self.fill(starting, sr, sc + 1, color, image)
        self.fill(starting, sr, sc - 1, color, image)

#python3 - 12/25/23 afternoon:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        self.fill(starting, image, sr, sc, color)
        return image
    def fill(self, starting, image, sr, sc, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color #actually flood it by flipping 1 to 2 - nothing to do with duplicate checking - this is not number of islands
        self.fill(starting, image, sr + 1, sc, color)
        self.fill(starting, image, sr - 1, sc, color)
        self.fill(starting, image, sr, sc + 1, color)
        self.fill(starting, image, sr, sc - 1, color)


#python3 - 12/25/23 evening solution refresher:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        self.fill(starting, image, sr, sc, color)
        return image
    def fill(self, starting, image, sr, sc, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color #WE HAVE TO ACTUALLY FLOOD FILL IT BY TURNING THE 1 - STARTING INTO A 2 - COLOR GIVEN. OR ELSE, IF WE DON'T DO THIS, WE WOULD BE FLOODING INFINTELY BECAUSE WE WOULD SEE THAT 1 THAT WILL ALWAYS BE A 1, SO WE WILL HAVE THAT TILE TO FILL FOREVER
        self.fill(starting, image, sr + 1, sc, color)
        self.fill(starting, image, sr - 1, sc, color)
        self.fill(starting, image, sr, sc + 1, color)
        self.fill(starting, image, sr, sc - 1, color)
        

#python3 - 12/26/12 refresher solution:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        self.fill(starting, image, sr, sc, color)
        return image
    def fill(self, starting, image, sr, sc, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting #if any tile is not equal to starting, we can't flood it, so we return nothing as the result to the function call that started it and then keep reading down one line of code from that function call:
            return
        image[sr][sc] = color # no infinite recursion - if we keep seeing 1, we will keep calling the function over and over again
        self.fill(starting, image, sr + 1, sc, color)
        self.fill(starting, image, sr - 1, sc, color)
        self.fill(starting, image, sr, sc + 1, color)
        self.fill(starting, image, sr, sc - 1, color)


#1/4/24 refresher solution:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        self.fill(image, sr, sc, color, starting)
        return image
    def fill(self, image, sr, sc, color, starting):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, color, starting)
        self.fill(image, sr - 1, sc, color, starting)
        self.fill(image, sr, sc + 1, color, starting)
        self.fill(image, sr, sc - 1, color, starting)

#1/6/24 refresher solution:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        self.fill(starting, image, sr, sc, color)
        return image
    def fill(self, starting, image, sr, sc, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[-1]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color
        self.fill(starting, image, sr + 1, sc, color)
        self.fill(starting, image, sr - 1, sc, color)
        self.fill(starting, image, sr, sc + 1, color)
        self.fill(starting, image, sr, sc - 1, color)


#1/17/24 refresher solution:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        #we can't even flip the starting tile, so there's no work to do, so our modified image after performing the flood fill is image
        if starting == color:
            return image
        #after we determine that we can flip the starting cell, we call the recursive function, which will try to flood in all 4 directions as long as the current cell has the same value as the starting color, so we pass in our current image, sr - wont change as given in input, sc - wont change as given in input, starting at image[sr][sc], and our color (won't change - given in input)
        self.fill(image, sr, sc, starting, color)
        return image
    def fill(self, image, sr, sc, starting, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, starting, color)
        self.fill(image, sr - 1, sc, starting, color)
        self.fill(image, sr, sc + 1, starting, color)
        self.fill(image, sr, sc - 1, starting, color)


#1/24/24 refresher practice solution:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        #if the 1st flip was successful, we start exploring adjacent cells to kickoff subsequent flips
        self.fill(image, sr, sc, color, starting)
        return image
    def fill(self, image, sr, sc, color, starting):
        #won't be true on 1st turn because we made it this far, so the 1st cell that kicks off subsequent flips will always be valid
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return 
        #we are not out of bounds, and this cell is equal to the starting color and can be flipped to the color to prevent infinite recursion
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, color, starting)
        self.fill(image, sr - 1, sc, color, starting)
        self.fill(image, sr, sc + 1, color, starting)
        self.fill(image, sr, sc - 1, color, starting)




#1/31/24 refresher:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        #no work to do because nothing kicked off explorations
        if starting == color:
            return image
        self.fill(image, sr, sc, starting, color)
        return image
    def fill(self, image, sr, sc, starting, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, starting, color)
        self.fill(image, sr - 1, sc, starting, color)
        self.fill(image, sr, sc + 1, starting, color)
        self.fill(image, sr, sc - 1, starting, color)


#2/6/24:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image
        self.fill(image, sr, sc, starting, color)
        return image
    def fill(self, image, sr, sc, starting, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color #won't be true on 1st turn since we already established that our starting pixel is NOT equal to color to even get here
        self.fill(image, sr + 1, sc, starting, color)
        self.fill(image, sr - 1, sc, starting, color) #will return to the def function and will start filling from the 1st recursive call with (sr + 1)
        self.fill(image, sr, sc + 1, starting, color)
        self.fill(image, sr, sc - 1, starting, color)

#2/15/24:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        #only can flood if the starting pixel is different from the color we want to change it to
        if starting == color:
            return image
        self.fill(image, sr, sc, starting, color)
        return image
    def fill(self, image, sr, sc, starting, color):
        #boundary check
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color #actually fill it so we don't run into infinite recursion trying to fill the same tile again and again
        self.fill(image, sr + 1, sc, starting, color)
        self.fill(image, sr - 1, sc, starting, color)
        self.fill(image, sr, sc + 1, starting, color)
        self.fill(image, sr, sc - 1, starting, color)


#3/9/24:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color: #if the starting pixel is already equal to the color pixel, then there is nothing to fill, and we can just return the image unmodified
            return image
        #if starting pixel is not equal to color, we have work to do, so we can start the process of filling adjacent cells
        self.fill(image, sr, sc, starting, color)
        return image
    def fill(self, image, sr, sc, starting, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting: #read the instructions carefull - we flood fill any tile that is equal to the starting cell only !
            return 
        image[sr][sc] = color 
        self.fill(image, sr + 1, sc, starting, color)
        self.fill(image, sr - 1, sc, starting, color)
        self.fill(image, sr, sc + 1, starting, color)
        self.fill(image, sr, sc - 1, starting, color)


#3/23/24:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc] 
        if starting == color:
            return image
        self.f(image, sr, sc, starting, color)
        return image
    def f(self, image, sr, sc, starting, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color
        self.f(image, sr + 1, sc, starting, color)
        self.f(image, sr - 1, sc, starting, color)
        self.f(image, sr, sc + 1, starting, color)
        self.f(image, sr, sc - 1, starting, color)

#4/21/24 refresher:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting == color:
            return image 
        self.fill(image, starting, sr, sc, color)
        return image
    def fill(self, image, starting, sr, sc, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != starting:
            return
        image[sr][sc] = color
        self.fill(image, starting, sr + 1, sc, color)
        self.fill(image, starting, sr - 1, sc, color)
        self.fill(image, starting, sr, sc + 1, color)
        self.fill(image, starting, sr, sc - 1, color)
