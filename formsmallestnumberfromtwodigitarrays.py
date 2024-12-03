

#2605
#easy

#Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.
 

#Example 1:

#Input: nums1 = [4,1,3], nums2 = [5,7]
#Output: 15
#Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
#Example 2:

#Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
#Output: 3
#Explanation: The number 3 contains the digit 3 which exists in both arrays.


#my own solution using python3:

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        first = Counter(nums1)
        second = Counter(nums2)
        a = set(nums1).intersection(set(nums2))
        if a:
            return min(a)
        new = []
        for a in nums1:
            for b in nums2:
                print(a, b)
                new.append(str(a) + str(b))
        print(new)
        for i, n in enumerate(new):
            new[i] = int(n)
        print(new)
        tmp = []
        for n in new:
            for a in permutations(str(n)):
                tmp.append("".join(a))
        print(tmp)
        for i, t in enumerate(tmp):
            tmp[i] = int(t)
        return min(tmp)
