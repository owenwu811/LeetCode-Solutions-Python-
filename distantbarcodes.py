
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


#correct python3 solution: (could not solve - this is a very good heap question to review!)

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        myheap = []
        for i, n in c.items():
            heapq.heappush(myheap, [-n, i])
        print(myheap)
        res = []
        while len(myheap) > 1:
            freq1, nums1 = heapq.heappop(myheap)
            freq2, nums2 = heapq.heappop(myheap)
            res.append(nums1)
            res.append(nums2)
            if (freq1 + 1) < 0:
                heapq.heappush(myheap, [freq1 + 1, nums1])
            if (freq2 + 1) < 0:
                heapq.heappush(myheap, [freq2 + 1, nums2])
        if myheap:
            res.append(myheap[0][1])
        return res
