You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1


Solution:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right: 
            mid = left + (right - left) // 2 #// prioritizes the left side of the array as mid
            if isBadVersion(mid): 
                right = mid
            else:
                left = mid + 1
        return left

   #this solution actually utilizes the two pointer approach and recursion to find the middle element, cutting the problem in a half and half again
   
   
6/11/2023 - we could also do right = mid - 1 if you include left <= right as we don't want to skip mid:

   # The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n #left starts at 1 because the first bad version can't be the first element in the list as all versions would be bad
        #we can garuntee that the last n value will always be bad, so that's why we will set right to n, or the last version, at the very least. 
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid): #if mid is a failed version, then search from the beginning to one less than mid because you know that the first bad version can't be to the right of mid at that point because the array is already sorted. When we search to the left of mid, the result will only update if mid is less. otherwise, we save that original mid value that made the function true in case that anything to the left of what mid was originally dosen't make the function true.
                right = mid - 1
            else:
                left = mid + 1
        return left

#after we find a mid that makes isBadVersion true, we will reduce the array's right to one left of mid and then add both left and right divided by 2 plus left again to calculate mid again in the reduced space


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

10/8/23 refresher solution (after looking at solution, I came up with some modifications and got the accepted solution below) - the key to remember is that ALL BAD VERSIONS AFTER THE FIRST BAD VERSION ARE ALSO BAD:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n 
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid): #is the current mid is a BadVersion aka isBadVersion(mid) turns out to be true, the actual FIRST bad version could be before mid, so we move right to mid minus one because, at the very least, right - 1 would HAVE to be the first bad version 
                r = mid - 1
            else: #we don't have a bad number to go by, so if isBadVersion(mid)
            #returns false, then we know that the bad version can't be before mid because all versions after a bad version are bad, so if isBadVersion(mid - 1) were true, than isBadVersion(mid) would be true, which it isn't, so if we 
            #know that the bad version isn't before the mid and isn't the mid, then, at best case, the first bad version could only be mid + 1, so we move the left pointer to mid + 1
                l = mid + 1
        return l #the reason we return left is because left represents the FIRST bad version aka the FIRST time that isBadVersion(mid) returns true


10/9/23 refresher (my own notes + thought process - please read):

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1 #if version 5 is mid and version 5 is good, then version 1 had to have been good software to have gotten up to 5's point because if 1 is bad, then 5 is bad because 5 comes after 1, so if 1 is good, then 5 is good, so if 5 is good, then 1 had to have been good because 5 builds on one, so if 5 is good, at best case, the first bad version has to be 6 at the best case, so move left pointer to 6 aka mid + 1 if mid is 5. 
        return l #we return left after l <= r is broken because left is always the smallest out of l, r, and mid, and if l and r cross, then that means right had to have been pulled down meaning that we had to have found a bad version because, for right to have been pulled down, we had to have called a bad version, so since l is the smallest, and l has atleast stepped on right but not overstepped, we know that l is at worst equal to r or l is smaller than r, which represnets the smallest numbered bad version aka the first version that returned true from the isBadVersion() function when everything before it returned false. the reason I am concluding that right had to have been pulled down aka bad version returned true for left and right to have overcrossed is because there always has to be a bad version, and for left to overcross aka make l <= r false, it must have come from the opposite direction and have crossed paths before overcrossing
        # if only the left pointer is moved (meaning only the else block is executed), the pointers l and r will indeed eventually cross. in the case of 1 2 3 l mid r. if only left is pulled up aka else is called, l and r will still cross and overcross. note that the problem's constraints tell us that there will always be a bad version
        #since there is guaranteed to always be a bad version, at worst case, the first bad version is the right most element, which, in this case, left will eventually hit by being pulled up over and over again aka the else block executed over again until they cross paths meaning that l will always eventually land on the first bad version



#1/24/24 refresher solution:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        #all versions after a bad version are bad, so if the current version is good, all previous versions must also be good
        #we want the first bad version
        smallest = 0
        largest = n
        #eliminating the search space using process of elimination
        while smallest <= largest:
            #use // 2 to round up so we don't get 3.5 instead of 4
            mid = (smallest + largest) // 2
            #if the current version is bad, there could be a version before the current causing the current to be bad, so we move largest pointer down to the previous one before the current since we want the first bad version
            if isBadVersion(mid):
                largest = mid - 1
            else:
                smallest = mid + 1
        return smallest
            

#2/4/24 refresher:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        #latest version (number) of product fails quality check. all versions after a bad version are bad, and all versions before a good version are good
        l = 0
        #n number of versions
        r = n
        #once left crosses right, we know we've used process of elimination to ensure the solution
        while l <= r:
            mid = (l + r) // 2
            #each number (left and right pointers are on number values) is either T (bad) or F(good)
            if isBadVersion(mid):
                r = mid - 1
            else: # current version is not bad, so previous ones couldn't have been bad since domino effect, so the first bad version earliest scenario is one to the right of mid, so close our search space
                l = mid + 1
        #we've narrowed down our search space, so left crossed right
        return l

#2/17/24 refresher:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        #all versions after a True version are bad
        #we want the first True number
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


#2/23/24:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
            
#3/1/24:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
