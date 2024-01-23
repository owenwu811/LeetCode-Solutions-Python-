
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
        #we need this below part because, for cases where we were always increasing monotonic (while loop never executed and we never popped meaning we never calculated the max area), we will need to calculate the maxarea - heights = [2, 4], for example
        for inputindex, inputvalue in stack:
            maxarea = max(maxarea, inputvalue * (len(heights) - inputindex))
        return maxarea
