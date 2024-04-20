#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Can you solve it without sorting?

#nums = [3,2,1,5,6,4], k = 2 - output = 5




#python3 solution:

#we use a minheap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k] #we get the first k elements in the input array not caring about what they are because we will compare later
        heapq.heapify(heap) #this is the size of k 
        for n in nums[k:]:
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
