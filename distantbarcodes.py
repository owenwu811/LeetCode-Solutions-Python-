
#medium
#1054

#In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

#Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.
 

#Example 1:

#Input: barcodes = [1,1,1,2,2,2]
#Output: [2,1,2,1,2,1]
#Example 2:

#Input: barcodes = [1,1,1,1,2,2,3,3]
#Output: [1,3,1,3,1,2,1,2]


#correct python3 solution: (could not solve - this is a very good heap question to review!) - similar to reorganize string!

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        myheap = []
        for i, n in c.items():
            heapq.heappush(myheap, [-n, i])
        print(myheap)
        res = []
        while len(myheap) > 1: #we should only attempt to pop two elements from the heap if there's atleast 2 elements available!
            freq1, nums1 = heapq.heappop(myheap) #we pop twice to ensure we aren't having the same neighboring values - we will add the valid frequencies back later with the two if blocks
            freq2, nums2 = heapq.heappop(myheap)
            res.append(nums1)
            res.append(nums2)
            if (freq1 + 1) < 0:
                heapq.heappush(myheap, [freq1 + 1, nums1]) # when you use heapq.heappush(myheap, [freq1 + 1, num1]), it automatically maintains the heap invariant without the need to call heapq.heapify(myheap) again
            if (freq2 + 1) < 0:
                heapq.heappush(myheap, [freq2 + 1, nums2])
        if myheap: #Once we process the heap until only one element remains (or no elements), we can handle it separately:
            #If there’s one element left in the heap, we can directly append it to the result list without worrying about adjacent duplicates, because it won’t have a neighbor to conflict with.
#If there are no elements left, the process is complete, and we can return the result.
            res.append(myheap[0][1])
        return res


#import heapq
#myheap = [[-1, 2], [-1, 3]]
#heapq.heapify(myheap)  # This is optional since we already have a valid heap

# Pop the smallest element
#smallest = heapq.heappop(myheap) - you will get [-1, 2] because 2 < 3 since -1 is the same!
