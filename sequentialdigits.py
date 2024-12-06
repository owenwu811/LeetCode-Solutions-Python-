

#1291
#medium

#An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

#Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

#Example 1:

#Input: low = 100, high = 300
#Output: [123,234]
#Example 2:

#Input: low = 1000, high = 13000
#Output: [1234,2345,3456,4567,5678,6789,12345]


#my own solution using python3:

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        options = "123456789"
        res = []
        for i in range(len(options)):
            for j in range(i, len(options)):
                substr = options[i: j + 1]
                print(substr)
                if low <= int(substr) <= high:
                    res.append(int(substr))
        res.sort()
        return res
