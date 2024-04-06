#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

 

#Example 1:

#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.
#Example 2:

#Input: s = "race a car"
#Output: false
#Explanation: "raceacar" is not a palindrome.
#Example 3:

#Input: s = " "
#Output: true
#Explanation: s is an empty string "" after removing non-alphanumeric characters.
#Since an empty string reads the same forward and backward, it is a palindrome.


#My Solution:

class Solution:
    def isPalindrome(self, s: str) -> bool:
#DO NOT CONFUSE S = S.REPLACE(CHARACTERTOREPLACE,REPLACEMENT,NUMBEROFTIMESTOREPLACEFROMBEG) WITH S = RE.SUB(PATTERN, REPLACEMENT, STRINGREPLACEMENTISPERFORMEDON)!!!!!
        s.replace(" ", "") #s.replace(old, new)
        s = re.sub('[\W_]', '', s) #re.sub(pattern, replacement, string). '[\W_]' patternmatches any character that isn't considered a word so that the replacement can replace the pattern. 
        start, end = 0, len(s) - 1 #indicies representing integers as starting and ending pointer
        while start < end: #make sure start and end don't cross 
            if s[start].casefold() != s[end].casefold(): #if, even after ignoring case, any starting character dosen't matching ending, we can automatically return false and say that it's not a perfect palindrome already
                return False
            start += 1 #if start and end chars do match, increment start and decrement end and ask the same question until you get to the middle of the string
            end -= 1
        return True #if, after we've gone through all characters starting on either side of the string and determined that they are all equal, then we do have a valid palindrome, so return True
        
# 6/9/23 refresher (my solution) - only 94/485 test cases passing - issue is that need to only keep alphanumeric characters and find middle index of string:
 
 class Solution:
    def isPalindrome(self, s: str) -> bool #- this approach is starting from the middle and expanding outwards and checking if they are the same until you reach the opposite ends:
        middle = len(s) / 2
        left, right = middle, middle
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        return True
                
                
#6/9/23 refresher (I also tried using a dictionary) - same 94/485 result - the issue is checking for only alphanumeric characters:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwarddict, backwarddict = {}, {}
        for i in s:
            forwarddict[s] = 0
        forwarddict[s] += 1
        for j in reversed(s):
            backwarddict[j] = 0
        backwarddict[j] += 1
        if forwarddict == backwarddict:
            return True
        else:
            return False

#12/25/23 refresher:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ", "")
        s = re.sub('[\W_]', "", s)
        l, r = 0, len(s) - 1
        #we know the last character is going to be the same as itself, so we don't need =, but having = works too in l <= r is valid too
        while l < r:
            #starting and ending must be equal because starting is ending's opposite, so if they are the same forward as backward, ending must also be starting's opposite, which they aren't if they aren't equal on both sides
            if s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        return True


#1/6/24 refresher solution:

s.replace(" ", "")
s = re.sub("[\W_]", "", s)
l, r = 0, len(s) - 1
while l < r:
    if s[l].casefold() != s[r].casefold():
        return False
    l += 1
    r -= 1
return True


#1/24/24 refresher:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s.replace(" ", "")
        s = re.sub("[\W_]", "", s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        return True


#2/3/24 refresher:
        #rid whitespaces
        s.replace(" ", "")
        #get rid of non alphanumeric characters
        s = re.sub('[\W_]', "", s)
        #we may be working with a smaller length s string now since we got rid of spaces and non alphanumeric characters
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        return True

#2/16/24:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we want case insensitive comparison
        s.replace(" ", "")
        #remove all non alphanumeric characters
        s = re.sub("[\W_]", "", s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        return True

#3/8/24:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all non alphanumeric characters and perform case insensitive check
        s = s.replace(" ", "")
        s = re.sub('[\W_]', "", s)
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        return True

#3/18/24:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub('[\W_]', "", s)
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        return True

#4/5/24:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub("[\W_]", "", s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        return True
