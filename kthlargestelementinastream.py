

#Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Implement KthLargest class:

#KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
#int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

#Example 1:

#Input
#["KthLargest", "add", "add", "add", "add", "add"]
#[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
#Output
#[null, 4, 5, 5, 8, 8]

#Explanation
#KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
#kthLargest.add(3);   // return 4
#kthLargest.add(5);   // return 5
#kthLargest.add(10);  // return 5
#kthLargest.add(9);   // return 8
#kthLargest.add(4);   // return 8

#python3 solution:

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []  # Min Heap
        for num in nums:
            heapq.heappush(self.minHeap, num)   # adding all elements to min heap
            
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)         # Only keeping k maximum elements so that we don't encounter an index out of bounds error
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)       # first add to min heap
        
        if len(self.minHeap) > self.k:          # if length greater pop minimum element as root is the min
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]                  # root is minHeap[0] as root is k'th max
    
# Time: O(N log(N))     # as heap size is N so heappush takes log(N) time
# Space: O(N)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
