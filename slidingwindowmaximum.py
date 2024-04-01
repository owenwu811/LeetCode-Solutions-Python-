#You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

#Return the max sliding window.

#nums = [1,3,-1,-3,5,3,6,7], k = 3
#output: [3,3,5,5,6,7]


#python3 solution:


class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = 0
        for r in range(len(nums)):
            #before adding 5 to our deque, we must check if 5 is greater than the value at top of deque. if it is, since 5 > 4, then don't consider 4 as max value ever again = [1, 1, 1, 1, 1, 4, 5], k = 6
            while q and nums[q[-1]] < nums[r]: 
                q.pop() #since we don't consider 4 as max value ever again since 5 > 4, pop 4 from deque
            q.append(r) #add 5 to the top 
            if l > q[0]: #[8, 7, 6, 9], k = 2. deque = [7, 6]. our window is [6, 9], so since 7 is no longer in bounds, and max value in our window is 7, we add 7 to the output before we pop 7 from our deque
                q.popleft() #the action of popping 7 from our deque
            if (r + 1) >= k: #edge case - since l and r both start from 0, we have to make sure our window is atleast size k to add to the output or update the output
                #for each iteration of the loop, for each window, we want to append our output with the maximum VALUE, so we need NUMS[Q[0]], not the index
                output.append(nums[q[0]]) #since our deque is always in decreasing order [8, 7], we can look at the leftmost value in our deque [8, 7] - 8 - and add 8 (leftmost) to our output
                l += 1 #left is only incremented once our window is atleast size k
            r += 1 # we don't actually need this line
        return output


#practice again:

class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = deque()
        l = 0
        for r in range(len(nums)):
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r) #indexes, not values, are appended to the deque
            if l > d[0]: #index comparison
                d.popleft()
            #edge case check
            if (r + 1) >= k:
                res.append(nums[d[0]])
                l += 1
        return res

#4/1/24:

class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #sliding window is of size k meaning you can only see k numbers in the window
        #we want to return the maximum number of each window of size k in order in a list
        res = []
        l = 0
        d = deque()
        for r in range(len(nums)):
            while d and nums[r] > nums[d[-1]]:
                d.pop() #useless
            d.append(r)
            if l > d[0]:
                d.popleft()
            if (r + 1) >= k:
                res.append(nums[d[0]]) #montonically dereasing queue
                l += 1
        return res

#practice again:

class Solution:
   def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #monotonically decreasing deque
        res = []
        l = 0
        d = deque()
        for r in range(len(nums)):
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r)
            if l > d[0]:
                d.popleft()
            if (r + 1) >= k:
                res.append(nums[d[0]])
                l += 1
        return res
