#You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

#Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

#Example 1:

#Input: letters = ["c","f","j"], target = "a"
#Output: "c"
#Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

#744
#easy
#52.6%acceptancerate



#my own solution using python3:

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
        return letters[0]
