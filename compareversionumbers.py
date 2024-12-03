
#165
#medium

#Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

#To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

#Return the following:

#If version1 < version2, return -1.
#If version1 > version2, return 1.
#Otherwise, return 0.
 

#Example 1:

#Input: version1 = "1.2", version2 = "1.10"

#Output: -1

#Explanation:

#version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

#Example 2:

#Input: version1 = "1.01", version2 = "1.001"

#Output: 0

#Explanation:

#Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

#Example 3:

#Input: version1 = "1.0", version2 = "1.0.0.0"

#Output: 0

#Explanation:

#version1 has less revisions, which means every missing revision are treated as "0".


#my own solution using python3:

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = version1.split(".")
        second = version2.split(".")
        #print(first, second)
        i, j = 0, 0
        while i < len(first) and j < len(second):
            if int(first[i]) > int(second[j]):
                return 1
            if int(second[j]) > int(first[i]):
                return -1
            i += 1
            j += 1
        print(i, j)
        print(first[i:])
        print(second[j:])
        if i < len(first) and not j < len(second):
            flag = False
            for w in first[i:]:
                if int(w) > 0:
                    flag = True 
            if flag:
                return 1
            if not flag:
                return 0
        if j < len(second) and not i < len(first):
            flag = False
            print(second[j:])
            for w in second[j:]:
                if int(w) > 0:
                    flag = True
            print(flag)
            if flag:
                return -1
            if not flag:
                return 0
        return 0
