#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

#Example 1:

#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:

#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
 

#Constraints:

#1 <= n <= 45

#My Solution:

#this is a classic dynamic programming problem

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 #regardless of how big or small n is, the first two pointers will always start at 1, and they will move left until one pointer is to the right of the output and two pointer is two to the right of the output
        #the 2nd pointer starts on the same element
        for i in range(n - 1): #8 - 1 = 7; range(7) = 0123456, so 8 - 6 to make room for 2 pointers
            temp = one 
            one = one + two #the result we will return before terminating case
            two = temp #two is set to one's previous value
        return one
        
  #line 35 is the one pointer
  #line 36 is the result of the terminating case (21 + 13)
  #line 37 is the two pointer
  #we are first calculating the sum of one and two pointer values, moving the two pointer into one, and then moving one pointer forward. During the terminating condition, thw two sandwiches with the one pointer, so both are equal, and then the for loop exits and returns the last calculated sum
  #[34 21 13 8 5 3 2 1 1]
  #                   one two
 #                    0    0
 #                    (inclusive)
  #[34 21 13 8 5 3 2 1 1]
  #     one two
  #     6   6
  #for i in range(8) means for i in range 01234567
  #when i hits 7, return one plus two pointer VALUES (13 + 21) - so, for this test case, n = 8, and the return value is 34
  #when i = 0, we initialize both pointer values as 1 and 1




#1/7/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n - 1):
            prev = one
            one = one + two
            two = prev
        return one


#1/12/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        oneway = 1
        secondway = 1
        #think of like fibonacci sequence
        for steps in range(n - 1):
            first = oneway
            oneway += secondway
            secondway = first
        return oneway


#1/17/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        #we want to find unique paths to the top, so we want the number of unique was to climb 0 steps all the way to n steps - similar to unique paths, but since we can only climb one or two steps, we can use two pointers
        one = 1
        two = 1
        #making room for two pointers
        for i in range(n - 1):
            storage = one
            one = one + two
            two = storage
        return one
        

#1/19/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        #there is always one way to climb the first step 
        one = 1
        two = 1
        #making room for two pointers
        for i in range(n - 1):
            nxt = one
            one = one + two
            two = nxt
        return one


#1/24/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        #since there is always one way to climb to the current staircase and 2 ways to climb, we have two pointers 
        one = 1
        two = 1
        #make room for 2 pointers
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


#1/29/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        #you can only climb 2 ways - 1 or 2 steps, so we can use two pointers
        one = 1
        two = 1
        #making room for both pointers - we will build up dynamic programming from left to right, sandwiching two with one
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        #this is similar to climbing stairs in that the one will return the number of unique ways to climb but except of bottom right to top left, we go from right to left by sandwiching second and first pointers
        return one

#2/14/24:

class Solution:
    def climbStairs(self, n: int) -> int:
        #you can climb 1 way or 2 ways
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        return one

#We start with one and two both equal to 1 because there is only one way to reach the first step (by taking one step) and the second step (by taking two steps).

We iterate n - 1 times because we've already accounted for the first step in our initialization. This loop calculates the number of distinct ways to reach each step up to the nth step.

This algorithm is efficient because it only requires O(n) time complexity and O(1) space complexity, making it suitable for large values of n.



#3/9/24:

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            r = one
            one = one + two
            two = r
        return one


#4/6/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        for i in range(n - 1):
            temp = first
            first = first + second
            second = temp
        return first


#5/1/24 refresher:

class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        for i in range(n - 1):
            temp = first
            first = first + second
            second = temp
        return first

#8/8/24 review:

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one


#10/19/24 review:

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            cur = one 
            one = one + two
            two = cur
        return one
