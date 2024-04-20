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
