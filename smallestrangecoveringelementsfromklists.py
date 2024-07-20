



#python3 solution with explanation:

class Solution:
    def smallestRange(self, nums):
        #n is assigned the length of nums, which is the number of lists in nums.
        #high is initialized to negative infinity. This will keep track of the maximum value in the current range.
        #minheap is an empty list that will be used as a min-heap (priority queue).
        #p is a list [0, float("inf")] representing the smallest range found so far, initialized to a very large range.
        inputlen, high, minheap, p = len(nums), float("-inf"), [], [0,float("inf")] #we initialize high to negative infinity so that when we compare any element, we know that any element will be bigger than negative infinity!
        for i in range(inputlen):
            #notice how we calculate high everytime we push a value onto the heap
            #root of heap is determined by smallest of nums[i][0]
            heapq.heappush(minheap,(nums[i][0],i,0))
            high = max(high,nums[i][0])
        while minheap: #while minheap here works too!
            #pop smallest element from root of minheap 
            low,i,idxinlist = heapq.heappop(minheap) #we don't know the lowst value of the 0th indexes of each sublist until we use the minheap to pop from the root - the point of the minheap is this!
            #After popping the smallest element, we check if the current range [low, high] (where low is the popped element) is smaller than the previously recorded smallest range p. If it is, we update p.
            current_range = high - low
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
