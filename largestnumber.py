
#Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

#Since the result may be very large, so you need to return a string instead of an integer.

#Example 1:

#Input: nums = [10,2]
#Output: "210"
#Example 2:

#Input: nums = [3,30,34,5,9]
#Output: "9534330"



#python3 solution:

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        def compare(n1, n2): #doing (n2, n1) will make the program fail if you don't adjust the right side of the equation of the if to match the order of the compare parameters
            #it seems as if n2 needs to come first, we always return 1 
            #regardless of if you do the 1 in the 1st block or 1 in 2nd block, n1 always starts at 30 and n2 always starts at 3
            if n2 + n1 > n1 + n2: #this means that n2 will come before n1 because we return 1 when the leftmost aka n2 comes first and the sign is going > way
                return 1
            else:
                return -1 #everytime we return -1, we backtrack, so [3,30,34,5,9] > n1 = 34, n2 = 30, so n1 + n2 > n2 + n1, so return -1, and then n1 = 34, and n2 becomes 3
        nums = sorted(nums, key=cmp_to_key(compare)) # so the compare function here can only have 2 arguments when using cmp_to_key because of the 1 and -1 rule of one coming before the other if bigger one return 1
        return str(int("".join(nums)))

        #b[3, 30, 34, 5, 9] - because 330 was the bigger path and 3430 was the bigger path, then we have to compare 34 to 3 since 3 went before 30 in their comparison and 34 went before 30 in their comparison, so we find out which one of the two bigger ones go first, so n1 = 34, n2 = 3, and since 34 was the one that goes first because 343 > 334, we compare 5(n1) to 3 next, and since 5 comes before 3, then we don't need to compare 3 anymore until we introduce a new number which may make 3 become the biggest number with that new number, so we comparing 5(n1) to 34, and since 5 comes before 34, we compare 9 to 3 because we introduced a new number of 9, and since 9 comes before 3, we don't even compare 9 to 30 because 30 was the loser between 3 and 34 coming after both of them, so we compare 9 to 34, and 9 comes before 34, so compare 9 to 5, and 9 comes before 5
        #also note that print(int(000)) > 0

#practice again:

class Solution:
    def largestNumber(self, nums):
        for index, value in enumerate(nums):
            nums[index] = str(value)
        def merge(n1, n2):
            if n2 + n1 > n1 + n2:
                return 1
            elif n2 + n1 < n1 + n2:
                return -1
            else:
                return 0
        nums = sorted(nums, key=cmp_to_key(merge))
        return str(int("".join(nums)))
        