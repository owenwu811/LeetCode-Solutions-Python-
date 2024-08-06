
#Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
#temperatures = [73,74,75,71,69,72,76,73]
#output: [1,1,4,2,1,1,0,0]
 


#python3 solution:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

#practice again:

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp) 
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                d = stack.pop()
                res[d] = i - d
            stack.append(i)
        return res

#3/29/24:

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res

#3/31/24:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res

#4/1/24:

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res

#4/4/24 practice:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #we want to return the number of days after current index to get a better temperature
        res = [0] * len(temperatures)
        d = deque() #we use a stack to keep track of the warmest temperature found so far
        for i in range(len(temperatures)):
            while d and temperatures[i] > temperatures[d[-1]]:
                a = d.pop() #a = 73
                res[a] = i - a
            d.append(i) #to rear of list
        return res

#4/5/24:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        d = deque()
        for i in range(len(temperatures)):
            while d and temperatures[i] > temperatures[d[-1]]:
                a = d.pop()
                res[a] = i - a
            d.append(i)
        return res

#4/7/24:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        d = deque()
        for i in range(len(temperatures)):
            while d and temperatures[i] > temperatures[d[-1]]:
                anwser = d.pop()
                res[anwser] = i - anwser

            d.append(i)
        return res


#4/19/24:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        d = deque()
        for i in range(len(temperatures)):
            while d and temperatures[i] > temperatures[d[-1]]:
                a = d.pop()
                res[a] = i - a
            d.append(i)
        return res


#4/27/24:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            #1st iteration, stack - [], so append 0 to rear of stack, and i becomes 1. 74 > 73, so stack [0] > [], and res[0] = 1 - 0, so res[0] = 1, and now we go back to call while loop, BUT STACK IS NOW [], SO THERE IS NOTHING TO COMPARE TO, SO ADD 1 to rear of stack! - notice how while is while stack AND temperatures[i] > temperatures[stack[-1]]
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i) 
        return res

#5/20/24 practice:

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res

#6/23/24 review (missed 2 days ago):

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res


#7/2/24 review:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res

#7/11/24 refresher:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #question says if there is no future day for which this is possible, keep anwser[i] == 0 instead
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res

#8/6/24 review:

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)
        return res
