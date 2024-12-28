

#831
#medium

#You are given a personal information string s, representing either an email address or a phone number. Return the masked personal information using the below rules.

#Email address:

#An email address is:

#A name consisting of uppercase and lowercase English letters, followed by
#The '@' symbol, followed by
#The domain consisting of uppercase and lowercase English letters with a dot '.' somewhere in the middle (not the first or last character).
#To mask an email:

#The uppercase letters in the name and domain must be converted to lowercase letters.
#The middle letters of the name (i.e., all but the first and last letters) must be replaced by 5 asterisks "*****".
#Phone number:

#A phone number is formatted as follows:

#The phone number contains 10-13 digits.
#The last 10 digits make up the local number.
#The remaining 0-3 digits, in the beginning, make up the country code.
#Separation characters from the set {'+', '-', '(', ')', ' '} separate the above digits in some way.
#To mask a phone number:

#Remove all separation characters.
#The masked phone number should have the form:
#"***-***-XXXX" if the country code has 0 digits.
#"+*-***-***-XXXX" if the country code has 1 digit.
#"+**-***-***-XXXX" if the country code has 2 digits.
#"+***-***-***-XXXX" if the country code has 3 digits.
#"XXXX" is the last 4 digits of the local number.
 

#Example 1:

#Input: s = "LeetCode@LeetCode.com"
#Output: "l*****e@leetcode.com"
#Explanation: s is an email address.
#The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.


#my own solution using python3:

class Solution:
    def maskPII(self, s: str) -> str:
        #s = "1(234)567-890"
        if "@" in s:
            location = []
            for i in range(len(s)):
                if s[i] == "@":
                    location.append(i)
            after = s[location[0] + 1:]
            afterlist = list(after)
            newlist = []
            for a in afterlist:
                if a.isalnum() and not (a.isdigit()):
                    newlist.append(a.lower())
                else:
                    newlist.append(a)
            goodsecondhalf = "".join(newlist)
            print(goodsecondhalf)
            before = s[:location[0] + 1]
            print(before)
            beforelist = list(before)
            newbeforelist = []
            for b in beforelist:
                if b.isalnum() and not (b.isdigit()):
                    newbeforelist.append(b.lower())
                else:
                    newbeforelist.append(b)
            print(newbeforelist)
            maskbefore = "".join(newbeforelist[:-1])
            newbefore = maskbefore[0]
            newafter = maskbefore[-1]
            maskedemail = newbefore + "*****" + newafter
            print(maskedemail)
            first, second, third = maskedemail, "@", goodsecondhalf
            return first + second + third
        else:
            #"1(234)567-890"
            digits = []
            for c in s:
                if c.isdigit():
                    digits.append(c)
            if len(digits) >= 10:
                diff = len(digits) - 10
                print(diff)
                if diff == 0:
                    firsth = "***-***-"
                    secondh = "".join(digits[-4:])
                    return firsth + secondh
                if diff == 1:
                    firsth = "+*-***-***-"
                    secondh = "".join(digits[-4:])
                    return firsth + secondh
                if diff == 2:
                    firsth = "+**-***-***-"
                    secondh = "".join(digits[-4:])
                    return firsth + secondh
                if diff == 3:
                    firsth = "+***-***-***-"
                    secondh = "".join(digits[-4:])
                    return firsth + secondh
