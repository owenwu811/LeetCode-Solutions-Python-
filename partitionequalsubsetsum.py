
#Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

#Example 1:

#Input: nums = [1,5,11,5]
#Output: true
#Explanation: The array can be partitioned as [1, 5, 5] and [11].


#python3 solution:


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subsums = set()
        subsums.add(0)
        half = sum(nums) // 2
        #the double for loop is for finding a subarray sum that is equal to half of the sum of nums aka target
        for inputnumber in nums:
            set2 = set()
            for subsumsn in subsums:
                set2.add(subsumsn + inputnumber)
                set2.add(subsumsn)
            subsums = set2
        return half in subsums
        #Since 22 is the sum of the nums, if we can find the subarray that is equal to the  target 11 then the sum of remaining nums always equal to the target 11.
        #mylist = [5] - print(5 in mylist) - True


#1/29/24 practice:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for number in nums:
            set2 = set()
            for element in subsum:
                set2.add(element + number)
                set2.add(element)
            subsum = set2
        return half in subsum

#1/31/24 practice:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       #we want two subSETS that are equal, so if one subset equals half the sum of nums, we know that it's possible
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        #not picking any elements starts with a sum of 0
        subsum.add(0)
        half = sum(nums) // 2
        for number in nums:
            set2 = set()
            for element in subsum:
                #including (left side)
                set2.add(element + number)
                #excluding (right side)
                set2.add(element)
            subsum = set2
        return half in subsum


#2/3/24 refresher solution:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #we want to find half of the sum inside of the current set that we create
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for number in nums:
            override = set()
            for numbers in subsum:
                override.add(number + numbers)
                override.add(numbers)
            subsum = override
        return half in subsum


#2/4/24 refresher:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #so if we can find one subset that is equal to half the sum of nums, then we know it's possible
        if sum(nums) % 2 > 0:
            return False
        #we want two subsets
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for inputnumber in nums:
            validationset = set()
            for s in subsum:
                validationset.add(s)
                validationset.add(s + inputnumber)
            subsum = validationset
        return half in subsum


#2/9/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for inputn in nums:
            set2 = set()
            for elements in subsum:
                set2.add(elements)
                set2.add(elements + inputn)
            subsum = set2
        return half in subsum


#2/10/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #there is a remainder when divided by 2, so we can't split into exactly 2 subsets with equal sums, so we return False
        if sum(nums) % 2 != 0:
            return False
        #if we just did return True here, we would fail #[1, 2, 5]
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for inputn in nums:
            set2 = set()
            for element in subsum:
                #the exclusion part is indirectly related to finding a subset whose sum equals half of the total sum of all elements.
                set2.add(element)
                set2.add(element + inputn)
            subsum = set2 #[0, 1], [0, 1, 2, 3], [0, 1, 2, 3, 5, 6, 7, 8] - 4 is not in this
        return half in subsum

        #[2, 3, 7, 8, 10] - half is 15, but that dosen't mean 15 has to be inside of the input list, so each set dosen't have to be a contiguous part of the array - [2, 3, 7, 8, 10] - 2 + 3 + 10 = 15 even though 2 and 3 and 10 aren't exactly right next to each other or connected
        #The goal is to find two subsets whose sums are equal, and these subsets can include elements from ANYWHERE in the original array, as long as their sums are equal.


#so if subsum eventually becomes [0, 1, 2, 3, 5, 6, 7, 8] for the [1, 2, 5] test case, then just because 3, 6, 7, and 8 aren't in the input is irrelevant because you can derive 3 from 1 + 2, 6 from 1 + 5, 7 from 5 + 2, and 8 from the whole thing (1 + 2 + 5), so we are indeed finding all combinations of different subsets in our input list by excluding and including - notice the subsets problem is similar in that it does the same thing and that this problem is called partition equal SUBSET sum, so if atleast one of the two subsets can, even once by taking some random combination of elements from input array and adding them toegether, equal half of the sum of nums, then we know that two halfs make a whole, so it's possible, so return True


#2/12/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #this is a variation of the add not add in subsets, but we just want two subsets that have equal sums, so this is dyamic programming
        #rule out possibilities if we have remainders when dividing total sum of all elements input by 2
        if sum(nums) % 2 != 0:
            return False
        #we need two sets
        subsum = set()
        #we don't want decimal division and want whole integers, so we use // instead of /
        half = sum(nums) // 2
        #acting as placeholder since set is empty but we also haven't summed anything in input
        subsum.add(0)
        for inputn in nums:
            set2 = set()
            for element in subsum:
                #this is the dynamic programming part where we include and don't include the current input into our sum to get every possible subset in the input - think about 3, 6, 7, and 8 from the [1, 2, 5] input example - 3 can be derived from 1 + 2, 5 is in the input list itself, 6 can be derived from 1 + 5...
                set2.add(element) #not including because element is 0 originally with only 1 iteration due to placeholder we created
                set2.add(element + inputn) # including
            subsum = set2
        return half in subsum

#2/17/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #not possible to split into two subsets with equal values
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0) #haven't picked any elements yet
        half = sum(nums) // 2 #don't want decimal
        for inputn in nums: #we loop through input array and, with each element, we either include or not include it 
            subset2 = set()
            for elements in subsum:
                subset2.add(elements) #don't include
                subset2.add(elements + inputn) #include
            subsum = subset2 #remember that, just because half of it is not inside the input array dosen't mean it won't be valid, so we need all possible subset sums of our input array to be computed
        return half in subsum


#2/26/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for inputn in nums:
            set2 = set()
            for element in subsum:
                set2.add(element)
                set2.add(element + inputn)
            subsum = set2
        return half in subsum

#2/29/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for inputn in nums:
            subset2 = set()
            for element in subsum:
                subset2.add(element)
                subset2.add(element + inputn)
            subsum = subset2
        return half in subsum

#3/4/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #2 subsets where sum of elements is equal - True - False otherwise
        if sum(nums) % 2 != 0:
            return False
        subsum = set()
        subsum.add(0)
        half = sum(nums) // 2
        for n in nums:
            subsum2 = set()
            for element in subsum:
                subsum2.add(element)
                subsum2.add(element + n)
            subsum = subsum2
        return half in subsum

#3/12/24:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #two subsets such that sum of elements in both subsets is equal
        if sum(nums) % 2 != 0:
            return False
        set1 = set()
        set1.add(0)
        half = sum(nums) // 2
        for number in nums:
            set2 = set()
            for element in set1:
                set2.add(element)
                set2.add(element + number)
            set1 = set2
        return half in set1
