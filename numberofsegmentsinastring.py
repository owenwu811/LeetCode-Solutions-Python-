

#434
#easy

#Given a string s, return the number of segments in the string.

#A segment is defined to be a contiguous sequence of non-space characters.

 

#Example 1:

#Input: s = "Hello, my name is John"
#Output: 5
#Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
#Example 2:

#Input: s = "Hello"
#Output: 1


#my own solution using python3:

class Solution:
    def countSegments(self, s: str) -> int:
        new = s.split(" ")
        print(new)
        actual = []
        for n in new:
            if n != "":
                actual.append(n)
        return len(actual)
