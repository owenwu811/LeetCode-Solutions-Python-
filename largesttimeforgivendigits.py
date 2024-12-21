
#949
#medium

#Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

#24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

#Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

 

#Example 1:

#Input: arr = [1,2,3,4]
#Output: "23:41"
#Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
#Example 2:

#Input: arr = [5,5,5,5]
#Output: ""
#Explanation: There are no valid 24-hour times as "55:55" is not valid.


#my own solution using python3:

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        c = []
        for a in permutations(arr):
            print(a)
            now = ""
            for h in a:
                now += str(h)
            #print(now)
            minutes = str(now[-2]) + str(now[-1])
            print(minutes)
            print(int(minutes))
            if int(now) < 2400 and int(minutes) < 60:
                print(now)
                c.append(now)
        c.sort()
        print(c)
        if not c:
            return ""
        ans = []
        for h in c[-1]:
            ans.append(h)
        ans.insert(2, ":")
        print(ans)
        return "".join(ans)
        

        
