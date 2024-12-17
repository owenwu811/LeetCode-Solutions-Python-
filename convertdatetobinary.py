
#3280
#easy

#You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

#date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

#Return the binary representation of date.

 

#Example 1:

#Input: date = "2080-02-29"

#Output: "100000100000-10-11101"

#Explanation:

#100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.



#my own solution using python3:

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d = date.split("-")
        indexes = []
        for i in range(len(date)):
            if date[i] == "-":
                indexes.append(i)
        print(d)
        actual = []
        for n in d:
            now = bin(int(n))
            after = str(now)[2:]
            actual.append(after)
        print(actual)
        new = ""
        for a in actual:
            new += a
            new += "-"
        return new[:-1]
