


#2358
#medium

#You are given a positive integer array grades which represents the grades of students in a university. You would like to enter all these students into a competition in ordered non-empty groups, such that the ordering meets the following conditions:

#The sum of the grades of students in the ith group is less than the sum of the grades of students in the (i + 1)th group, for all groups (except the last).
#The total number of students in the ith group is less than the total number of students in the (i + 1)th group, for all groups (except the last).
#Return the maximum number of groups that can be formed.

 

#Example 1:

#Input: grades = [10,6,12,7,3,5]
#Output: 3
#Explanation: The following is a possible way to form 3 groups of students:
#- 1st group has the students with grades = [12]. Sum of grades: 12. Student count: 1
#- 2nd group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
#- 3rd group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
#It can be shown that it is not possible to form more than 3 groups.


#my own solution using python3:

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        orig = 1
        actual = []
        tmp = []
        while orig <= len(grades):
            tmp = []
            j = orig
            while j > 0:
                tmp.append(grades.pop())
                j -= 1
            actual.append(tmp)
            orig += 1
        return len(actual)
        print(actual)



#my other solution using python3:

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        tmp, actual = [], []
        orig = 1
        myheap = []
        for g in grades:
            heapq.heappush(myheap, -g)
        while orig <= len(myheap):
            j = orig
            tmp = []
            while j > 0:
                if not myheap:
                    break
                tmp.append(-1 * heapq.heappop(myheap))
                j -= 1
            orig += 1
            actual.append(tmp)
        print(actual)
        return len(actual)

            
