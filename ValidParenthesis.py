Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Solution: 

#use a list to simulate a stack
#a mismatch of characters in the stack means that the top character is different, which automatically invalidates all True cases
#at every iteration in s, we either pop from the stack (True up to this point) or return False (mismatch)
#the stack will never have more than one symbol in it because we either return False due to incorrect opening complement or don't add current and pop the correct complement from the stack if True until that point

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        opening_brackets = "({["
        closing_brackets = ")}]"
        for char in s:
            if char in opening_brackets: #if char in opening_brackets checks if the character char is present in the opening_brackets list anywhere, not just at the same index as the for char in s.
                stack.append(char)
            #closing characters {[( can't be the same as opening )]}, so either if is true or elif is true, not both
            elif char in closing_brackets: #if there is not a corresponding opening bracket, and the stack (current characters in s so far) is empty, then there is not a valid parenthesis.
                if not stack:
                    return False
                #by default, .pop() pops from the end of the list
                opening_bracket = stack.pop() #if there is a match, then we don't add the closing to the stack and instead pop the opening from the stack.
                #we did find an opening character aka didn't reach end of s yet, but it's a mismatch, so not valid parenthesis, so you can return False
                #by this line, we will never come across a closing bracket in s because we either returned false already because we didn't find valid match or because we popped a valid pair off
                if opening_brackets.index(opening_bracket) != closing_brackets.index(char): #anything leftover in the stack after iterating through s, return false because there are unpaired characters.
                    return False
        return not stack #stack is empty, so all symbols are matched, so return True. NOT STACK == TRUE MEANS STACK IS EMPTY WHILE NOT STACK == FALSE MEANS THE STACK STILL HAS UNMATCHED CHARACTERS, SO RETURN FALSE. EITHER WAY, THIS LINE WILL RETURN A BOOLEAN AT THE END OF EITHER TRUE OR FALSE.
        
 #the idea is that ][ is not a valid parenthesis, but [] is
 #if we encounter a closing bracket ], and there isn't already an opening bracket [ in front of it in s, then it's automatically false
 #the reason you can't do if char in closing_brackets elif char in opening_brackets is because () is valid but )( is not valid. If the first is (, then you wouldn't have a matching opening.
 
 
 Solution 6/8/23 refresh:
 
 class Solution:
    def isValid(self, s: str) -> bool:   
        result = []
        opening_brackets, closing_brackets = "([{", ")]}"
        for char in s:
            if char in opening_brackets:
                result.append(char)
            elif char in closing_brackets and not result: #if the current iteration character is a closing bracket and result list is empty, that means we don't have any matches because the first character in the string is a closing bracket, and }{ or )( or ][ dosen't count as true
                return False
            else:
                opening_bracket = result.pop()
                if opening_brackets.index(opening_bracket) != closing_brackets.index(char):  #my mistake was that I was trying to index into opening_bracket instead of opening_brackets, so I need to give a more descriptive variable name to opening_bracket = result.pop() - makesurematchesthis?
                    return False
        return not result

My Solution 7/1/23 refresh:

class Solution:
    def isValid(self, s: str) -> bool:   
        stack = []
        openbrackets = "({[" #these are all possibilities of opening brackets that we can have 
        closebrackets = ")}]" #make sure the corresponding closing bracket is at the same index in this string as in openbrackets
        for values in s:
            if values in openbrackets:
                stack.append(values)
            elif values in closebrackets and not stack: #stack is empty, and )( dosen't count as valid, so return False
                return False
            else:
                complement = stack.pop() #we have found a closing bracket and want to find the corresponding opening bracket 
                if openbrackets.index(complement) != closebrackets.index(values): #make sure we are lining up values with closebrackets.index because this case has a close bracket and tries to find an opening bracket since not stack was false, meaning there were still characters in the stack, so it's still a possibility to be true to continue onto the next iteration of the for loop
                    return False
        return not stack #the stack should be empty is every pair has exactly one complement, so this is a boolean

My Solution 9/29/23 refresh:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ob = "({["
        cb = ")}]"
        for char in s:
            if char in ob:
                stack.append(char)
            elif char in cb and not stack:
                return False 
            else:
                complementto = stack.pop()
                if ob.index(complementto) != cb.index(char):
                    return False
        return not stack


my solution 11/10/23 refresh:

class Solution:
    def isValid(self, s: str) -> bool:
        matchmaker = []
        openingb = "([{"
        closingb = ")]}"
        for current in s:
            if current in openingb:
                matchmaker.append(current)
            elif current in closingb and not matchmaker:
                return False
            elif current in closingb and matchmaker: #current in closingb and matchmaker list has open brackets inside of it
                potentialopeningmatch = matchmaker.pop()
                if openingb.index(potentialopeningmatch) != closingb.index(current):
                    return False
        return not matchmaker


my solution 12/26/23 refresher:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb = "({["
        closeb = ")}]"
        for char in s:
            if char in openb: #only girls go on the stack in order
                stack.append(char) #stack.append is first in last out
            elif char in closeb and not stack: #too many boys or boys come first because )( is not the right order
                return False
            else:
                girl = stack.pop()
                if openb.index(girl) != closeb.index(char):
                    return False
        #False if too many girls
        return not stack



#1/4/24 refresher solution:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb = "({["
        closeb = ")}]"
        for bracket in s:
            if bracket in openb:
                stack.append(bracket)
            elif bracket in closeb and not stack:
                return False
            else:
                girl = stack.pop()
                if openb.index(girl) != closeb.index(bracket):
                    return False
        return not stack 



#1/17/24 refresher solution:

class Solution:
    def isValid(self, s: str) -> bool:
        #our input string only has 3 types of brackets inside of it
        #valid = True = same type of brackets + no closed before opening + equal frequency of brackets of each type
        openb = "({["
        closeb = ")}]"
        stack = []
        for char in s:
            if char in openb:
                stack.append(char)
            #too many boys or boy comes first before ever seeing girl meaning we have a misstmatch already
            elif char in closeb and not stack:
                return False
            else: #char in closeb(char is a boy) and there are girls
                girl = stack.pop()
                if openb.index(girl) != closeb.index(char):
                    return False
        return not stack


#1/24/24 refresher practice:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb = "({["
        closeb = ")}]"
        for bracket in s:
            if bracket in openb:
                stack.append(bracket)
            elif bracket in closeb and not stack:
                return False
            else:
                girl = stack.pop()
                if openb.index(girl) != closeb.index(bracket):
                    return False
        return not stack

#2/16/24:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb = "{(["
        closeb = "})]"
        for char in s:
            if char in openb:
                stack.append(char)
            elif char in closeb and not stack:
                return False
            else:
                girl = stack.pop()
                if openb.index(girl) != closeb.index(char):
                    return False
        return not stack



#3/10/24:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb, closeb = "{([", "})]"
        for char in s:
            if char in openb: #only girls go on the rear of the stack
                stack.append(char)
            elif char in closeb and not stack: #)( or }{ or ][ isn't valid aka we have too many boys
                return False 
            else: #char most be in closeb since if covered all scenarios for openb
                girl = stack.pop() #sets the popped bracket equal to a variable called girl
                if openb.index(girl) != closeb.index(char): return False
        return not stack #only False if extra openb or extra girls at the end

                

#3/18/24:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb, closeb = "({[", ")}]"
        for char in s:
            if char in openb:
                stack.append(char)
            elif char in closeb and not stack:
                return False 
            else: #seeing a closeb 
                girl = stack.pop()
                if openb.index(girl) != closeb.index(char):
                    return False
        return not stack


#4/22/24:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb = "({["
        closeb = ")}]"
        for char in s:
            if char in openb:
                stack.append(char)
            elif char in closeb and not stack:
                return False
            else:
                o = stack.pop()
                if openb.index(o) != closeb.index(char):
                    return False
        return not stack


#5/19/24 practice:

class Solution:
    def isValid(self, s: str) -> bool:
        openb, closeb = "({[", ")}]"
        stack = []
        for char in s:
            if char in openb:
                stack.append(char)
            elif char in closeb and not stack:
                return False
            else: #closeb and stack
                girl = stack.pop()
                if openb.index(girl) != closeb.index(char):
                    return False
        return not stack


#7/26/24 refresher:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb, closeb = "({[", ")}]"
        for char in s:
            if char in openb:
                stack.append(char)
            elif char in closeb and not stack:
                return False
            else:
                c = stack.pop()
                if openb.index(c) != closeb.index(char):
                    return False
        return not stack
