
#easy
#65.3% acceptance rate

#Given a string s, reverse the string according to the following rules:

#All the characters that are not English letters remain in the same position.
#All the English letters (lowercase or uppercase) should be reversed.
#Return s after reversing it.

 

#Example 1:

#Input: s = "ab-cd"
#Output: "dc-ba"
#Example 2:

#Input: s = "a-bC-dEf-ghIj"
#Output: "j-Ih-gfE-dCba"
#Example 3:

#Input: s = "Test1ng-Leet=code-Q!"
#Output: "Qedo1ct-eeLg=ntse-T!"

#my own solution using python3 after taking hint of two pointer:

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
        print(stack)
        l, r = 0, len(stack) - 1
        while l < r:
            if stack[l].isalpha() and stack[r].isalpha():
                stack[l], stack[r] = stack[r], stack[l]
                l += 1
                r -= 1
            elif stack[l].isalpha() and not (stack[r].isalpha()):
                r -= 1
            else:
                l += 1
        return "".join(stack)
        
