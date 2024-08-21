



#python3 solution with explanation:

class Solution:
    def smallestRange(self, nums):
        #high is initialized to negative infinity. This will keep track of the maximum value in the current range because any range value we add is bigger than negative infinity
        #minheap is an empty list that will be used as a min-heap (priority queue).
        #p is a list [0, float("inf")] representing the smallest range found so far, initialized to a very large range.
        #the reason we have inputlen is because we need to know how many sublists in our input list of lists we have, so inputlen is the assigned length of nums, which is the number of lists in nums
        inputlen, high, minheap, p = len(nums), float("-inf"), [], [0,float("inf")] #we initialize high to negative infinity so that when we compare any element, we know that any element will be bigger than negative infinity!
        for i in range(inputlen):
            #notice how we calculate high everytime we push a value onto the heap
            #root of heap is determined by smallest of nums[i][0]
            heapq.heappush(minheap,(nums[i][0],i,0)) #notice here how the last element of the tuple stays at 0 because we stay on the same vertical to add elements to the minheap!
            high = max(high,nums[i][0])
        while minheap: #while minheap here works too!
            #pop smallest element from root of minheap 
            low,i,idxinlist = heapq.heappop(minheap) #we don't know the lowst value of the 0th indexes of each sublist until we use the minheap to pop from the root - the point of the minheap is this!
            #After popping the smallest element, we check if the current range [low, high] (where low is the popped element) is smaller than the previously recorded smallest range p. If it is, we update p.
            current_range = high - low #now that we actually know what the smallest value out of the 0th indexes (atleast on 1st iteration) of each sublist in our input list of lists is, we can now calculate the current range!
            if p[1]-p[0] > current_range: #p[1] is infinity and p[0] is 0 in the first turn, so infinity - 0 = infinity, and any range from the 0th indexes of all our sublists will be smaller than infinity when we take the highest of the 0th indexes - the smallest of the 0th indexes from each sublist in our input list of lists!
                p = [low,high]
            #If the popped element is the last element in its list, the function returns p because it's not possible to extend the range further from this list.
            #the problem specifically requires that each range must include elements from all three lists. With List 1 exhausted, it's impossible to form a valid range that includes elements from all lists. Therefore, any range formed after this point cannot meet the problem's requirement and is considered invalid.
            if idxinlist == len(nums[i])-1: 
                return p
            #After popping the smallest element from list i, we push the next element from the same list i onto the heap. This ensures that we always maintain a range that includes elements from all lists.
            heapq.heappush(minheap,(nums[i][idxinlist+1],i,idxinlist+1))
            #Whenever we push a new element onto the heap, we update high to be the maximum of the current high and the new element. This step ensures high is always the maximum element among the elements currently considered in the range.
            high = max(high,nums[i][idxinlist+1])

        #this solution looks eerily similr to kth smallest element in a sorted 


#7/20/24 review:

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        inputlen, high, minheap, res = len(nums), float('-inf'), [], [0, float('inf')] 
        for i in range(inputlen):
            heapq.heappush(minheap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])
        while minheap:
            low, i, idxinlist = heapq.heappop(minheap)
            current_range = high - low
            if current_range < res[1] - res[0]:
                res = [low, high]
            if idxinlist == len(nums[i]) - 1:
                return res
            heapq.heappush(minheap, (nums[i][idxinlist + 1], i, idxinlist + 1))
            high = max(high, nums[i][idxinlist + 1])

#7/21/24 refresher:

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        inputlen, res, high, minheap = len(nums), [0, float('inf')], float('-inf'), []
        for i in range(inputlen):
            heapq.heappush(minheap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])
        while minheap:
            low, i, indexinlist = heapq.heappop(minheap)
            current_range = high - low
            if current_range < res[1] - res[0]:
                res = [low, high]
            if indexinlist == len(nums[i]) - 1: #remember the all lists requirement in our res list upper and lower value range
                return res
            heapq.heappush(minheap, (nums[i][indexinlist + 1], i, indexinlist + 1))
            high = max(high, nums[i][indexinlist + 1])


#7/23/24 review:

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        inputlen, ans, high, myheap = len(nums), [0, float('inf')], float('-inf'), []
        for i in range(inputlen):
            heapq.heappush(myheap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])
        while myheap:
            low, index, listindex = heapq.heappop(myheap)
            current_range = high - low
            if current_range < ans[1] - ans[0]:
                ans = [low, high]
            if listindex >= len(nums[index]) - 1:
                return ans
            heapq.heappush(myheap, (nums[index][listindex + 1], index, listindex + 1))
            high = max(high, nums[index][listindex + 1])

#7/28/24 refresher:

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        inputlen, res, high, minheap = len(nums), [0, float('inf')], float('-inf'), []
        for i in range(inputlen):
            heapq.heappush(minheap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])
        while minheap:
            low, i, indexinlist = heapq.heappop(minheap) #make sure i here and not index because then the below heappush would read from an incorrect variable!
            print(low)
            current_range = high - low
            if res[1] - res[0] > current_range:
                res = [low, high]
            print(res)
            if indexinlist >= len(nums[i]) - 1:
                return res
            heapq.heappush(minheap, (nums[i][indexinlist + 1], i, indexinlist + 1))
            high = max(high, nums[i][indexinlist + 1])


#8/21/24 review (missed):

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minheap = []
        inputlen, p, high = len(nums), [0, float('inf')], float('-inf')
        for i in range(inputlen):
            heapq.heappush(minheap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])
        while minheap:
            low, i, idxinlist = heapq.heappop(minheap)
            currentrange = high - low
            if p[1] - p[0] > currentrange:
                p = [low, high]
            if idxinlist >= len(nums[i]) - 1:
                return p
            heapq.heappush(minheap, (nums[i][idxinlist + 1], i, idxinlist + 1))
            high = max(high, nums[i][idxinlist + 1])

#practice again on 8/21/24:

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        inputlen = len(nums)
        minheap = []
        p = [0, float('inf')]
        high = float('-inf')
        for i in range(inputlen):
            heapq.heappush(minheap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])
        while minheap:
            low, i, idxinlist = heapq.heappop(minheap)
            currentrange = high - low
            if p[1] - p[0] > currentrange:
                p = [low, high]
            if idxinlist >= len(nums[i]) - 1:
                return p
            heapq.heappush(minheap, (nums[i][idxinlist + 1], i, idxinlist + 1))
            high = max(high, nums[i][idxinlist + 1])

        
