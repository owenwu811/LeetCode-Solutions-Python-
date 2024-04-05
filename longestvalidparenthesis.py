#Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
#substring
#.

 

#Example 1:

#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".




#python3 solution:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]  #[-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) #stack contains indicies
            #")()())" > output = 4
            else: #1st iteration is ), so not (, so stack.pop() > []. not stack is True, so we append 0 index to the stack > [0]. we keep iterating, so i becomes 1. s[i] is equal to "(", so append 1 (index) to the stack - [0, 1]. we keep iterating, so i becomes 2.s[2] is ")", which is not "(", so we pop from stack. stack goes from [0, 1] to [0]. if not stack is False since stack still has [0] inside of it, so we can take maxlength, which is max(0, 2 - 0), so maxlength becomes 2, representing "()" from indexes 1 and 2 - ")()())". we get 2 - 0 because i = 2, and stack[-1] = 0 since there is only one element on the stack. Next, i becomes 3. s[3] = "(", so append index 3 to the stack ( stack goes from [0] to [0, 3]), and keep iterating for loop, so i becomes 4, and s[4] = ")", which is not "(", so pop from stack - [0] becomes [0, 3]. if not stack is False because we still have [0] in the stack, so maxlength is updated with max(2, 4 - 0), so maxlength becomes 4. i = 4, and stack[-1] = 0 to get maxlength. for loop i now becomes 5, so s[5] = ")", which is not "(", so pop from stack - stack goes from [0] to []. if not stack is now True, so we append index 5 to the stack. stack goes from [] to [5]. for loop now terminates, so return maxlength of 4 
            
                stack.pop()
                if not stack: #not stack handles when more ) than (
                    stack.append(i) 
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length
s = ")()())"
solution = Solution()
print(solution.longestValidParentheses(s))

#note that stack = [0] instead of stack = [-1] would fail "()" test case, giving us 1 instead of 2 because maxlength would be doing i - stack[-1], which is 1 - 0 instead of 1 - - 1. 

#the reason we do stack[-1] is because we are minusing the index by stack[-1] to update maxlength, which counts the current opening bracket because only opening brackets go in the stack as + 1 to the maxlength


#4/5/24 practice: missed

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(": 
                stack.append(i)
            else:
                stack.pop() #"(()" means [-1, 0, 1] becomes [-1, 0]
                if not stack: #true if 1st char is ")" in s, so 0 goes to rear of stack, and anything minus 0 is that number without hurt, so that's why ) first in s dosen't count as part of result
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1]) #2 - 0 = 2
        return res

