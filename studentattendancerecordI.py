#551
#easy

#You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

#'A': Absent.
#'L': Late.
#'P': Present.
#The student is eligible for an attendance award if they meet both of the following criteria:

#The student was absent ('A') for strictly fewer than 2 days total.
#The student was never late ('L') for 3 or more consecutive days.
#Return true if the student is eligible for an attendance award, or false otherwise.

 

#Example 1:

#Input: s = "PPALLP"
#Output: true
#Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.


#my own solution using python3:

class Solution:
    def checkRecord(self, s: str) -> bool:
        absent, late, present = [], [], []
        for i, c in enumerate(s):
            if c == "A":
                absent.append(i)
            if c == "L":
                late.append(i)
        print(late)
        flag = True
        for i in range(len(late) - 2):
            subarr = late[i: i + 3]
            print(subarr)
            if subarr[0] + 1 == subarr[1] and subarr[1] + 1 == subarr[2]:
                flag = False
        return len(absent) < 2 and flag
