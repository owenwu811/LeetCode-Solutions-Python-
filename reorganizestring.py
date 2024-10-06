

#767
#medium

#Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

#Return any possible rearrangement of s or return "" if not possible.

 
#Example 1:

#Input: s = "aab"
#Output: "aba"
#Example 2:

#Input: s = "aaab"
#Output: ""


#my own solution using python3 after a few fixes from edge cases: (THIS QUESTION IS THE SAME AS DISTANT BARCODES!)

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        if max(c.values()) > (len(s) + 1) // 2:
            return ""
        myheap = []
        for i, n in c.items():
            heapq.heappush(myheap, [-n, i])
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
        return "".join(res)
