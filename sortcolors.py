Given an array, colors, which contains a combination of the following three elements:

#0
#0
 (representing red)
#1
#1
 (representing white)
#2
#2
 (representing blue)
Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.


#My Solution (Python):

def sort_colors(colors):

    red, white, blue = 0, 0, len(colors) - 1
    #for white in range(blue):
    #[102122]
    #blue = 5
    #i = 0,1,2,3,4, so must add 1 because range without + 1 would terminate right before the actual flip in a case where color = [0, 1, 0] because i would be 0, 1 before terminating while the len(blue) would be 2, and we want to flip the index 1's 1 with index 2's 0 to go from [0, 1, 0] to [0, 0, 1]
    for i in range((blue) + 1):
        if colors[white] == 0 and white <= blue:
            colors[white], colors[red] = colors[red], colors[white]
            white += 1
            red += 1
        elif colors[white] == 1 and white <= blue:
            white += 1
    
        elif colors[white] == 2 and white <= blue:
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1
            
    return colors


#Grokking's Solution (Python):

def sort_colors(colors):

    # Replace this placeholder return statement with your code
    red, white, blue = 0, 0, len(colors) - 1
    #for white in range(blue):
    #[102122]
    #blue = 5
    #i = 0,1,2,3,4
    while white <= blue:
        if colors[white] == 0 and white <= blue:
            colors[white], colors[red] = colors[red], colors[white]
            white += 1
            red += 1
        elif colors[white] == 1 and white <= blue:
            white += 1
    
        elif colors[white] == 2 and white <= blue:
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1
            
    return colors


#python3 solution:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        n = 0 #n is going to represnet the point at which everything up to including n is sorted in order, and when the n > r, the while loop terminates aka when n is on 2 and r is on 1, representing all numbers from 0 up to and including 2 being sorted in order
        while n <= r:
            if nums[n] == 2:
                nums[n], nums[r] = nums[r], nums[n]
                r -= 1
            elif nums[n] == 1:
                n += 1 #n will go from a 1 to a 0 and then will get flipped next turn because we only have 0s and 1s and 2s in our array because next iteration will look like [1, 0, 2]
                                                                                                                                                                                l  r/c
            else:
                nums[n], nums[l] = nums[l], nums[n]
                n += 1
                l += 1


#my solution python3 - 12/24/23 refresher:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        uptosorted = 0
        end = len(nums) - 1
        while uptosorted <= end: #by the time this is violated, end will be on a 1 and uptosorted will be on a 2, indicating everything up to 2 is sorted
            if nums[uptosorted] == 2:
                nums[uptosorted], nums[end] = nums[end], nums[uptosorted]
                end -= 1
            elif nums[uptosorted] == 1:
                uptosorted += 1
            else:
                nums[uptosorted], nums[start] = nums[start], nums[uptosorted]
                uptosorted += 1
                start += 1


#my solution - python3 - 1/7/24 refresher:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        #nuetral pointer represents the point at which all numbers up to including nuetral are sorted (nuetral is also an index into the array starting at 0)
        n = 0
        right = len(nums) - 1
        while n <= right:
            #we are only given 0s, 1s, and 2s in our input array nums
            if nums[n] == 2:
                nums[n], nums[right] = nums[right], nums[n]
                right -= 1
            elif nums[n] == 1:
                n += 1
            elif nums[n] == 0:
                #the bug I made this time was a typo - nums[left], nums[n] on the right side of the equation instead of the inverse as intended
                nums[left], nums[n] = nums[n], nums[left]
                left += 1
                n += 1



#1/11/24 refresher solution:

l = 0
r = len(nums) - 1
c = 0
while c <= r:
    if nums[c] == 2:
        #the order of r or c or c or r first dosen't matter as long as they are swapped
        nums[r], nums[c] = nums[c], nums[r]
        r -= 1
    elif nums[c] == 1:
        c += 1
    else:
        #the order of c or l or l or c first dosen't matter as long as they are swapped 
        nums[l], nums[c] = nums[c], nums[l]
        l += 1
        c += 1


#1/16/24 refresher solution:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        l = 0
        r = len(nums) - 1
        #if c crosses to the right of r, then we've sorted all numbers in the array
        while c <= r:
            if nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            elif nums[c] == 1:
                c += 1
            else:
                nums[l], nums[c] = nums[c], nums[l]
                l += 1
                c += 1



#1/24/24 refresher:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        c = 0
        r = len(nums) - 1
        while c <= r:
            if nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            elif nums[c] == 1:
                c += 1
            else:
                nums[l], nums[c] = nums[c], nums[l]
                l += 1
                c += 1
                


#1/29/24 refresher:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        n = 0
        #everything up to nuetral is already sorted
        while n <= r:
            if nums[n] == 2:
                nums[n], nums[r] = nums[r], nums[n]
                r -= 1
            elif nums[n] == 1:
                n += 1
            elif nums[n] == 0:
                nums[l], nums[n] = nums[n], nums[l]
                n += 1
                l += 1 


#2/4/24 refresher solution:

#indicies (one less than length)
        l, r = 0, len(nums) - 1
        n = 0 #the point is that the array is not already sorted, and it's your job to sort it, so that's why n can't start at mid because we wouldn't even know what mid is equal to 
        while n <= r:
            if nums[n] == 2:
                nums[n], nums[r] = nums[r], nums[n]
                r -= 1
            elif nums[n] == 1:
                n += 1
            else: #we know we only have 0s and 1s and 2s
                nums[l], nums[n] = nums[n], nums[l]
                n += 1
                l += 1

#2/11/24 practice:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        l, r, n = 0, len(nums) - 1, 0
        while n <= r: #everything up to and including n is sorted, so when n crosses r, we know everything in the array is sorted since r also moves down if n and r are swapped
            if nums[n] == 2:
                nums[n], nums[r] = nums[r], nums[n]
                r -= 1
            elif nums[n] == 1:
                n += 1
            elif nums[n] == 0:
                nums[l], nums[n] = nums[n], nums[l]
                l += 1
                n += 1
            

#2/21/24:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        l, r = 0, len(nums) - 1
        n = 0
        while n <= r:
            if nums[n] == 2:
                nums[n], nums[r] = nums[r], nums[n]
                r -= 1
            elif nums[n] == 1:
                n += 1
            else:
                nums[l], nums[n] = nums[n], nums[l]
                l += 1
                n += 1

#3/25/24:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, c, r = 0, 0, len(nums) - 1
        while c <= r: #c <= r because when c and r cross, we've sorted everything up to count!!!
            if nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            elif nums[c] == 1:
                c += 1
            elif nums[c] == 0:
                nums[l], nums[c] = nums[c], nums[l]
                c += 1
                l += 1

#4/5/24:

class Solution:
    def sortColors(self, nums: List[int]) -> None: #this is the dutch national flag problem
        """
        Do not return anything, modify nums in-place instead.
        """ 
        #we know we are only given 0s and 1s and 2s, so we can use process of elimination
        l, c = 0, 0
        r = len(nums) - 1
        while c <= r:
            if nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            elif nums[c] == 1:
                c += 1
            else:
                nums[l], nums[c] = nums[c], nums[l]
                l += 1 
                c += 1
        

#4/14/24:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
         #we know we only have 0 or 1 or 2a
         l, r = 0, len(nums) - 1
         c = 0
         while c <= r: #c represents point at which all elements up to including c are already in sorted order
            if nums[c] == 2: 
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            elif nums[c] == 1:
                c += 1
            else:
                nums[c], nums[l] = nums[l], nums[c]
                l += 1
                c += 1

#5/10/24 refresher:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        #we know we are only given 0s and 1s and 2s, so we can use process of elimination
        l, c = 0, 0
        r = len(nums) - 1
        while c <= r:
            if nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            elif nums[c] == 1:
                c += 1
            else:
                nums[l], nums[c] = nums[c], nums[l]
                l += 1
                c += 1
