#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Can you solve it without sorting?

#nums = [3,2,1,5,6,4], k = 2 - output = 5




#python3 solution:

#we use a minheap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k] #we get the first k elements in the input array not caring about what they are because we will compare later, so if k = 4, we get heap = indexes 0 through 3 inclusive
        heapq.heapify(heap) #this is the size of k 
        for n in nums[k:]: #looping through nums[4:], so [1, 5, 6, 4], and we wil compare the 0th heap element with each element in [1, 5, 6, 4], and if the 0th heap is smaller, then we will pop from top of heap since that element is no longer part of k largest elements and isn't possible to be part of smallest out of k largest elements (what we are ultimately looking for) and then add the current element out of [1, 5, 6, 4] to the heap maintaining the heap invariant 
            if heap[0] < n:
                heapq.heappop(heap) #pull from top of heap
                heapq.heappush(heap, n) #pushes element onto the heap maintaining the heap invariant, not having anything to do with pushing onto rear!
        return heap[0] #we want the smallest element inside of the k largest elements including duplicates
      
      #The min-heap contains the k largest elements seen from the array at the end 
      #root of the min-heap (heap[0]) is the smallest of these k largest elements
      #we are looking for the k-th largest element, heap[0] at the end will indeed be this smallest element among the k largest

     #so if nums = [3, 2, 1, 5, 6, 4], k = 2, we get [3, 2] > [2, 3], and then for loop n goes over each element in [1, 5, 6, 4]
     #we then as is 2 < 1, no, so keep iterating to n = 5. is 2 < 5 - yes, so the heap goes from [2, 3] to [3, 5] since we pop from top (smallest in heap) and then heappush to maintain heap invariant, adding the current n to maintain the heap invariant
     #we keep looping so n = 6. is 3 < 6 - yes, so heap goes from [3, 5] to [5, 6] - we kick out 3 because we know 3 is no longer possible to be within the kth largest elements because heap is of size k and will have the largest k elements in the array in the end
     #we then keep looping so n = 4. 5 < 4 is false, so return heap[0], which is 5


    #for test case nums = [3,2,3,1,2,4,5,5,6], k = 4, note that the output would be 4 because both 5s are counted, so duplicates count!
    #heap = [3, 2, 3, 1] > [1, 2, 3, 3]
    # [2, 4, 5, 5, 6] - n will loop through 
    #so when n equals the 1st 5, heap goes from [2, 3, 3, 4] to [3, 3, 4, 5] because the 2 is no longer part of the k largest elements, and we want to find the smallest of the k largest elements in the end
    #when n equals the 2nd 5, heap goes from [3, 3, 4, 5] to [3, 5, 4, 5] - because 3 is no longer part of the k largest elements, we pop 3 off because we always pop the smallest element off the top of a minheap, and [3, 5, 4, 5] is the result after heappush, so heaps can have duplicates! - notice the heap invariant here hasn't been reshuffled yet until the next iteration
    #when n equals 6 (last iteration), heap goes from [3, 5, 4, 5] to [4, 5, 5, 6], and the result will be 4 (heap[0])


#review again:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]

#4/21/24:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we want the smallest element of the k largest elements in the array - k meaning length
        heap = nums[:k] #size k with 1st k length elements in the input array
        heapq.heapify(heap)
        for n in nums[k:]: 
            if heap[0] < n: #if true, not part of k largest, so evict
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]

#4/21/24 practice again:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]


#4/23/24:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]

#4/24/24 review:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]


#4/26/24 refresher:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we want the smallest element out of the k largest elements in the input array
        heap = nums[:k] #size k
        heapq.heapify(heap) #smallest is at top
        for n in nums[k:]:
            if heap[0] < n: #if true, we know the smallest aka root of heap cannot be part of k largest, so we pop and add our n according to heap invariant
                heapq.heappop(heap)
                heapq.heappush(heap, n) 
        return heap[0]


#5/8/24 refresher:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #[3, 2, 1, 5, 6, 4] > [2, 3, 1, 5, 6, 4]
        #we want the smallest of the k largest
        firstk = nums[:k] #we want this to be of size k 
        heapq.heapify(firstk) #[3, 2] becomes [2, 3]
        for n in nums[k:]: #[1, 5, 6, 4]
            if n > firstk[0]:
                heapq.heappop(firstk)
                heapq.heappush(firstk, n)
        return firstk[0]


#5/19/24 practice:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we want the smallest element from the k largest elements including duplicates
        arr = nums[:k]
        heapq.heapify(arr)
        #[2, 3]
        for n in nums[k:]:
            if n > arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr, n)
        return arr[0]
        

#6/17/24 review:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #out of the k largest elements in the array, we want the smallest element in sorted order
        heap = nums[:k]
        heapq.heapify(heap) #[3, 2] > [2, 3]
        for n in nums[k:]: #[1, 5, 6, 4]
            if n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]


#7/16/24 refresher (my own solution):

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we want to find the smallest element of the kth largest elements in the array
        myheap = []
        for n in nums[:k]:
            heapq.heappush(myheap, n)
        heapq.heapify(myheap)
        #[2, 3]
        for remaining in nums[k:]:
            if remaining > myheap[0]:
                heapq.heappop(myheap)
                heapq.heappush(myheap, remaining)
        return myheap[0]


#8/23/24 review:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myheap = []
        for n in nums[:k]:
            heapq.heappush(myheap, n)
        print(myheap)
        for n in nums[k:]:
            if n > myheap[0]:
                heapq.heappop(myheap)
                heapq.heappush(myheap, n)
        return myheap[0]


#my own solution using python3 - 10/18/24 review:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        return nums[-k]

