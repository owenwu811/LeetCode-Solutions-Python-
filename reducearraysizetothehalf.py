

#1338

#You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

#Return the minimum size of the set so that at least half of the integers of the array are removed.

 

#Example 1:

#Input: arr = [3,3,3,3,5,5,5,2,2,7]
#Output: 2
#Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
#Possible sets of size 2 are {3,5},{3,2},{5,2}.
#Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
#Example 2:

#Input: arr = [7,7,7,7,7,7]
#Output: 1
#Explanation: The only possible set you can choose is {7}. This will make the new array empty.


#my own solution using python3 after looking at solution and borrowing elements from it:

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        startlen = len(arr)
        mydict = dict()
        for a in arr:
            if a not in mydict:
                mydict[a] = 0
            mydict[a] += 1
        myheap = []
        for k in mydict:
            heapq.heappush(myheap, -mydict[k])
        print(myheap)
        origlen = startlen
        turn = 0
        while origlen > startlen // 2:
            origlen -= -heapq.heappop(myheap)
            turn += 1
        return turn


#another one of my solutions:

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        origlen = len(arr)
        mydict = dict()
        for a in arr:
            if a not in mydict:
                mydict[a] = 0
            mydict[a] += 1
        myheap = []
        for k in mydict:
            heapq.heappush(myheap, -mydict[k])
        res = 0
        changinglen = origlen
        while changinglen > origlen // 2:
            changinglen -= -heapq.heappop(myheap) #we are always subtracting the mostfrequent element from our length to find the minimum size of set aka least number of turns the game has until atleast half are removed
            res += 1
        return res
