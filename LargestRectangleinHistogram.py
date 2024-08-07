
#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
#Input: heights = [2,1,5,6,2,3]
#Output: 10
#Explanation: The above is a histogram where width of each bar is 1.
#The largest rectangle is shown in the red area, which has an area = 10 units.






#python3 solution:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #our end result
        maxarea = 0
        #this problem requires an increasing monotonic stack where, if the previous value in our input array is greater than our current value we are iterating over, we pop from the stack until the monotonicly increasing aspect of it is restored
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            #reflecting the change of starting a new window after a violation of a monotonically increasing aspect
            #starting a new window at index 2 in heights = [2,1,5,6,2,3], so startindex will become 2
            startindex = inputindex
            #we want to monotonical increasing stack - when it stops being a monotonic stack, the while loop inner block executes
            #will always be false in 1st iteration since nothing was ever added to the stack and so there is no stack[-1][1] that exists
            while stack and stack[-1][1] > inputvalue:
                ##keep popping until we are still a monotonic stack
                stackindex, stackheightvalue = stack.pop()
                maxarea = max(maxarea, stackheightvalue * (inputindex - stackindex))
                #if this wasn't stackindex and was set to inputindex, we wouldn't be accurately reflecting the loss in progress due to the next element being less than current or montonically increasing aspect violated
                startindex = stackindex
            #we are still an increasing monotonic, so append to stack
            stack.append((startindex, inputvalue))
        # #truly increasing montonic because everything that was not increasing monotonic was popped - even values that are equal 
        #we need this below part because, for cases where we were always increasing monotonic (while loop never executed and we never popped meaning we never calculated the max area), we will need to calculate the maxarea - heights = [2, 4], for example. but stack = [(0, 2), (1, 4)], so res for test case heights = [2, 4] is 4
        for inputindex, inputvalue in stack:
            maxarea = max(maxarea, inputvalue * (len(heights) - inputindex))
        return maxarea


#practice run:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        #we need a monotonicly increasing stack
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            #this is needed to accurately convey the start of a new window 
            startindex = inputindex
            while stack and stack[-1][1] > inputvalue:
                #we violated our monotonic stack increasing, so we pop until we don't violate our montonoic increasing stack
                stackindex, stackheightvalue = stack.pop()
                #for each frame that we pop, we calculate the max area because that frame ended
                maxarea = max(maxarea, stackheightvalue * (inputindex - stackindex))
                startindex = stackindex
            stack.append((startindex, inputvalue))
        #if we never violated our montonic increasing stack, we never popped, so we also never calculated the maxarea
        for i, j in stack:
            maxarea = max(maxarea, j * (len(heights) - i))
        return maxarea


#practice run 1/23/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        #we need an increasing monotonic stack
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            start = inputindex
            #we have violated our monotonically increasing quality
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                start = stackindex
            stack.append((start, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res


#1/26/24 practice run:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #this problem requires an increasing monotonic stack where, as soon as the montonically increasing quality is violated, we pop off the stack and calculate the area
        stack = []
        res = 0
        for inputindex, inputvalue in enumerate(heights):
            startofwindow = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                startofwindow = stackindex
            stack.append((startofwindow, inputvalue))
        for actualindex, actualvalue in stack:
            res = max(res, actualvalue * (len(heights) - actualindex))
        return res



#1/29/24 practice:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for inputindex, inputvalue in enumerate(heights):
            starting = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                starting = stackindex
            stack.append((starting, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res


#another practice run:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        #we want a monotonically increasing stack 
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            starting = inputindex
            while len(stack) > 0 and stack[-1][1] > inputvalue:
                #monotonically increasing property is violated since we have something at the back of our stack that's less than our current input number in heights, so the new bar is less than the old bar, so we want to keep popping until that monotonically increasing property is restored - remember that current has to be larger than previous bar - equal would still be violating the monotonically increasing property
                #we keep popping and calculating 5 and 6 bar heights before 1 and 2 bar heights
                stackindex, stackheight = stack.pop()
                #after we restored our monotonically increasing property, we know everything in the stack follows the monotonic property, so the stackindex now represents the point starting where we are following the property and inputindex is the currentindex that, previously wasn't following monotonic property but now is, so we take the stack height times the inputindex - stackindex
                res = max(res, stackheight * (inputindex - stackindex))
                #we now start a new window at the new stackindex
                starting = stackindex
            #as long as not violating monotonic property, keep appending to rear of stack list in order 
            stack.append((starting, inputvalue))
        #we have gone through the input array once, so we know that everything that wasn't monotonically increasing has been corrected, so everything in the stack is now monotonically increasing, so we can compute the width times height for each possibility in our stack
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res



#2/2/24 refresher:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #for this problem, we need a monotonic increasing stack because, as soon as we reach a bar height that is more than the previous bar height, we want to keep popping
        stack = []
        res = 0
        for inputindex, inputvalue in enumerate(heights):
            start = inputindex
            while stack and stack[-1][1] > inputvalue:
                #monotonically increasing quality is violated, so we want to keep popping
                stackindex, stackheight = stack.pop()
                #we want the width as the distance up until the monotonic quality was violated, so we subtract the current inputindex minus stackindex, with stackindex being the last viable solution - if we used (starting - stackindex), we would get 5 * (3 - 2) instead of 5 * (4 - 2) for the test case heights = [2,1,5,6,2,3], and the - for i, j in stack - block would actually turn res into 8 with 2 * (6 - 2), which is wrong as we we want 10 as the result
                res = max(res, stackheight * (inputindex - stackindex))
                start = stackindex
            stack.append((start, inputvalue))
        #now that we know our stack dosen't violate our monotonic quality, we can multiply the entire width of our new stack
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#not including the - for i, j in stack - block would fail the test case [2, 4], returning 0 as res instead of 4 since the - while stack and stack[-1][1] > inputvalue - line never executes, so we never actually calculate res since it was alsready fitting a monotonic quality, so we need this to catch it



#2/9/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for stackindex, stackvalue in enumerate(heights):
            start = stackindex
            while stack and stack[-1][1] > stackvalue:
                myindex, myvalue = stack.pop()
                res = max(res, myvalue * (stackindex - myindex))
                start = myindex
            stack.append((start, stackvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#2/18/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            start = inputindex
            while stack and inputvalue < stack[-1][1]: 
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                start = stackindex
            #if you did stack.append([inputindex, inputvalue]) instead of [start, inputvalue], you would fail test case [2, 1, 2] because you would add [1, 1] to stack instead of [0, 1], so you don't want just the current index but the start of a potential rectangle 
            stack.append([start, inputvalue])
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#2/22/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            starting = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                starting = stackindex

            stack.append((starting, inputvalue))
        for x, y in stack:
            res = max(res, y * (len(heights) - x))
        return res


#2/25/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            start = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                start = stackindex
            stack.append((start, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#3/1/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            start = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                start = stackindex
            stack.append((start, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res


#3/4/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        monotonicstack = []
        for inputindex, inputvalue in enumerate(heights):
            starting = inputindex
            while monotonicstack and monotonicstack[-1][1] >= inputvalue: #>= works too instead of just > because equals means montonic quality is being violated
                stackindex, stackheight = monotonicstack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                starting = stackindex
            monotonicstack.append([starting, inputvalue])
        for i, j in monotonicstack:
            res = max(res, j * (len(heights) - i))
        return res

#3/11/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #width of each bar = 1
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            validstarting = inputindex
            #violated our monotonic condition
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackvalue = stack.pop()
                res = max(res, stackvalue * (inputindex - stackindex))
                validstarting = stackindex
            stack.append((validstarting, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#3/16/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] 
        for inputindex, inputval in enumerate(heights):
            starting = inputindex
            while stack and stack[-1][1] > inputval:
                stackindex, stackval = stack.pop()
                res = max(res, stackval * (inputindex - stackindex))
                starting = stackindex #If we were to set starting to inputindex instead of stackindex, it would result in an incorrect calculation of the width of the rectangle. This would lead to incorrect width calculation, as the rectangle's width should be measured from the index of the popped element to the current index, not from the current index to itself!
            stack.append((starting, inputval))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#We'll focus on the fifth iteration, where inputval = 2 and we encounter a situation where inputval < stack[-1][1].

#heights = [2, 1, 5, 6, 2, 3]
           #0  1  2  3  4  5

#Original Code (setting starting to stackindex):

#Before the fifth iteration, the stack contains (2, 5) and (3, 6).
#When popping (3, 6), starting is set to 3.
#The width of the rectangle is correctly calculated as 4 - 3 = 1.
#Modified Code (setting starting to inputindex):

#Before the fifth iteration, the stack contains (2, 5) and (3, 6).
#When popping (3, 6), starting remains 4 (current inputindex).
#The width of the rectangle would then be calculated as 4 - 4 = 0.
#This difference leads to an incorrect width calculation. The rectangle's width should be measured from the index of the popped element (3, 6) to the current index 4, not from the current index to itself. Therefore, setting starting = inputindex in this scenario would result in an incorrect calculation of the width of the rectangle and subsequently an incorrect calculation of the maximum area.


#3/21/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            starting = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackvalue = stack.pop()
                res = max(res, stackvalue * (inputindex - stackindex))
                starting = stackindex
            stack.append((starting, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res


#3/27/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            starting = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                starting = stackindex
            stack.append((starting, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i)) #remember parenthesis around len(heights) - i !!!!
        return res

        #[(0, 2), (1, 1)]

#4/10/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] #monotonic increasing stack
        for inputindex, inputvalue in enumerate(heights):
            starting = inputindex
            while stack and inputvalue <= stack[-1][1]:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                starting = stackindex
            stack.append((starting, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#5/6/24:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            start = inputindex
            while stack and stack[-1][1] > inputvalue:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                start = stackindex
            stack.append((start, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res
        
#5/28/24 review:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            current = inputindex
            while stack and inputvalue < stack[-1][1]:
                stackindex, stackheight = stack.pop()
                res = max(res, stackheight * (inputindex - stackindex))
                current = stackindex
            stack.append((current, inputvalue))
        for i, j in stack:
            res = max(res, j * (len(heights) - i))
        return res

#6/22/24 review:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputvalue in enumerate(heights):
            startingindex = inputindex
            while stack and inputvalue < stack[-1][1]:
                stackindex, stackvalue = stack.pop() #0, 2
                res = max(res, stackvalue * (inputindex - stackindex)) #1 * ()
                print(res)
                startingindex = stackindex
            stack.append((startingindex, inputvalue)) #[(0, 2)]
        print(stack)
        for i, j in stack: 
            res = max(res, j * (len(heights) - i)) #even though input heights array may be longer than stack, we are just going through the stack and then using the input array as the bigger length to subtract from. we are not indexing into the bigger array
            #1 * (2 - 0) = 2
        return res

#for [2, 1, 2] case, expected = 3. if you did:
for i, j in stack:
    res = max(res, j * len(stack) - i))

#instead of 
for i, j in stack:
    res = max(res, j * len(heights) - i))

#you would get 2 as output instead of 3. 
#stack in end = [(0, 1), (2, 2)]
#wrong anwser would be 1 * (2 - 0) with len(stack) - i
#correct anwser would be 1 * (3 - 0) with len(heights) - i

# .   .
# . . .

#we can't do:
for i, j in enumerate(stack):
    res = max(res, j[1] * (len(heights) - i))
#because that would give us 4 because i would be 1 instead of 2, so we would get 2 * 2 instead of 2 * 1 for the last iteration, giving us an output of 4 instead of 3

for i, j in enumerate(stack):
    res = max(res, j * len(heights) - i))
#above is invalid because j = (0, 1) not a number

#enumerate's i ALWAYS goes from 0 to 1 to 2 !!!!!!

#7/23/24 review:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for inputindex, inputheight in enumerate(heights):
            start = inputindex
            while stack and inputheight < stack[-1][1]:
                stackindex, stackheight = stack.pop()
                res = max(res, (inputindex - stackindex) * stackheight)
                start = stackindex
            stack.append((start, inputheight))
        print(stack)
        for i, j in stack:
            print(i, j)
            res = max(res, j * (len(heights) - i))
            print(res)
        return res
        #[2, 1, 2]
        #[1  1. 1] = 3

        #[(1, 1), (2, 2)]
        #1 * (3 - 1)
                
