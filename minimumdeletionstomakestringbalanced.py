
#You are given a string s consisting only of characters 'a' and 'b'​​​​.

#You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

#Return the minimum number of deletions needed to make s balanced.


#A string is considered balanced if there are no instances of 'a' appearing after 'b'.
#As we iterate through the string, we encounter two types of characters: 'a' and 'b'.

#Logic:

#As we iterate through the string, we encounter two types of characters: 'a' and 'b'.
#If we encounter an 'a', we have two choices:
#Either delete this 'a', which increases the minDeletions count by 1.
#Or, consider the number of 'b's we've seen so far (bCount), and assume we delete those 'b's to balance the string at this point.
#We choose the minimum of these two options (min(minDeletions + 1, bCount)) to ensure the least number of deletions.
#If we encounter a 'b', we simply increment bCount as it might be needed for comparison with future 'a's.

#Input: s = "aababbab"
#Output: 2
#Explanation: You can either:
#Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
#Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").


#my own solution using python3 after looking at solution:

class Solution:
    def minimumDeletions(self, s: str) -> int:
        bc, res = 0, 0
        for char in s:
            if char == "b":
                bc += 1
            else:
                res = min(res + 1, bc)
        return res
            
