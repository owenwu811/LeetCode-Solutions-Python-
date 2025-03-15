#14
#easy


#Write a function to find the longest common prefix string amongst an array of strings.

 #If there is no common prefix, return an empty string "".

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:

#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
 
#Constraints:

#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lowercase English letters.


#my own solution using python3 on 3/15/25:

#find all prefixes of the 1st string, and if all other strings have that prefix, update result accordingly

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            cur = strs[0]
            for j in range(len(cur)):
                pref = cur[:j + 1]
                cnt = 0
                for word in strs[1:]:
                    if word.startswith(pref):
                        cnt += 1
                if cnt == len(strs) - 1:
                    if len(pref) >= len(res):
                        res = pref
        return res



#Python Solution (with my explanation):

class Solution:
   def longestCommonPrefix(self, strs: List[str]) -> str:
      res = ""
      for i in range(len(strs[0])):
        for s in strs:
          if i == len(s) or s[i] != strs[0][i]:
            return res
          res += strs[0][i]
      return res

#(NOTE THAT CAPITALIZED LETTERS INDICATE THE CHARACTER IN THE SUBSTRING BEING COMPARED, SO PAY CLOSE ATTENTION TO THEM)
#​​Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Line 4: for i in range(len(“flower”))

#for i in range(6) > i = 0, 1, 2, 3, 4, 5 as integer indexes 

#Line 5: for s in strs

#s = “flower” during 1st iteration 

#I = 0, so if 0 == 6 (length of flower) or 

#S = “flower”
#I = 0
#S[i] = s[0]
#S[0] = f 
#S[i] in this iteration = f
#I = 0
#Strs[0][i] = strs[0][0]
#Strs[0][0] in this iteration = ["Flower","flow","flight"]
#If i == len(s) > if 0 == 6 - false or s[i] != strs[0][i] > f != f - false - the if conditional is false, so go back up to line 5
#S = ["flower","FLOW","flight"]
#i is still 0, so if 0 == 4 (not) or f != f (not because s[i] - the i hasn’t changed yet until it hits line 4)
#Go back up to line 5
#S = [“flower”, “flow”, “FLIGHT”]
#If i == len(s) - 0 == 6 (not) or s[i] != strs[0][i] (not because s[i] hasn’t changed yet until line 4 gets executed)
#Go back up to line 5
#For s in strs reaches end of loop, so execute line 8
#Res += strs[0][i]
#“” += ["Flower","flow","flight"]
#Res becomes “f”
#NOW, LINE 4 FOR LOOP GETS EXECUTED
#For i in range(len(strs[0])) - i goes from 0 > 1
#I = 1
#For s in strs > s = ["FLOWER","flow","flight"]
#If i == len(s) becomes 1 == 6 (false) or s[i] != strs[0][i] becomes 
#["fLower","flow","fLight"] !=  ["flower","flow","flight"] (false)
#So go back to line 5
#For s in strs - s becomes ["flower","FLOW","flight"]
#If i == len(s) becomes if 1 == 4 (false) or s[i] != strs[0][1] becomes 
#["fower","fLow","flight"] != ["fLower","flow","flight"] (false) so go back to line 5
#For s in strs > s = ["flower","flow","FLIGHT"]
#If i == len(s) becomes 1 == 6 (false) or s[i] != strs[0][i] becomes 
#["flower","flow","fLight"] != ["fLower","flow","flight"] (false)
#For s in strs - hits end of loop, so execute line 8
#Res += strs[0][i] 
#“F” += “L”
#Res becomes “fL”
#For i in range(len(strs[0])) gets executed again > i goes from 1 to 2, so i = 2
#For s in strs > s = ["FLOWER","flow","flight"] (s resets because for s in strs comes after for i in range line)
#If i == len(s) becomes 2 == 6 (false) or s[i] != strs[0][i] becomes 
#["flOwer","flow","flight"] != ["flOwer","flow","flight"] (false), so go back and execute line 5
#For s in strs > s =  ["flower","FLOW","flight"]
#If i == len(s) or s[i] != strs[0][i]
#If 2 == 4 (not) or ["flower","flOw","flight"] !=  ["flOwer","flow","flight"] (false)
#Go back to line 5
#For s in strs > s =  ["flower","flow","FLIGHT"]
#If i == len(s) or s[i] != strs[0][i]
#If 2 == 6 (not) or ["flower","flow","flIght"] != ["flOwer","flow","flight"] (true), so return res as “fl”


#Mistakes from not paying attention:


#S = ["FLOWER","flow","flight"] in line 5 for the first iteration is different than:
#Strs = ["flower","flow","flight"] always being the entire string itself!!! Don’t confuse the two!!!


#For s in strs > s =  ["flower","flow","flight"]
#If i == len(s) or s[i] != strs[0][i]
#If 2 == 4 (not) or ["flower","flow","flight"] !=  ["flower","flow","flight"] (false)


#In the 2nd iteration of for s in strs, s = ["flower","flow","flight"], so if 2 == 4, not 2 == 6 anymore because S CHANGES WHILE STRS STAYS CONSTANT !!!!!!!!!


-----



#Why are we doing strs[o][i]???



#Notice above that flower stays constant in all 3 comparisons! Aka representing s[i] != strs[0][i]


#Notice above that flower stays constant in all 3 comparisons! Aka representing s[i] != strs[0][i] (STRS[0] CONSTANT PART)


#As soon as if in line 6 turns true, we return res because that’s when we find a difference aka violating the condition of the substring comparison being equal


#What if the first part becomes true but 2nd is false? if i == len(s) or s[i] != strs[0][i]:


#If i == len(s) becomes true, then return true because we’ve covered the entire length of the substring - ["flower","flow","flight"], for example - and we are only as strong or equal as our weakest (shortest) member in this case?


#I == len(s) means if the index in the non changing strs = ["flower","flow","flight"] surpasses the entire length of the substring s = ["flower","flow","flight"] - meaning i would be out of boundaries for comparison between s and strs inside of strs, and we can’t do the comparison




#Notice how line 4 strs[0] is the same as line 6 strs[0][i], so we may be using this as the static string to be compared to


#We cannot substitute strs[0] in lines 4, 6, and 8 with strs[1] or strs[2] because it would be out of the index of i, which starts at 0 - I PROVED MY ASSUMPTION TRUE BECAUSE using strs[-1] in lines 4, 6, and 8 works!!!

#The reason strs[-2] in lines 4, 6, and 8 dosen’t work is probably because it gives us the same substring in the list as strs[0] given that the list is of length 3 substrings - ["flower","flow","flight"] (both strs[0] and strs[-2] are "flower")

#NOTE (MY SOLUTION ALSO WORKS - YOU CAN DO res += strs[0][i] or s[i] since both need to line up and neither is more important than the other)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "" #the solution starts by defining an empty string that we will add to character by character 
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += s[i] #works too instead of res ++ strs[0][i]
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


#if i == len(s) means that your anwser key INDEX is out of bounds of either one of the 3 strings that exist in the list because they're supposed to be matched as they both come from strs and indexes are 1 less than string length, so if they are equal, there's a problem
# like if i = 5 as the last of "flower" anwser key while len(s) = 6 for "flight", we're fine
# but if i = 5 as the last of "flower" anwser key while len(s) = 5 for "flows", then "flower" would be overstepping "flows", so the biggest match out of ALL 3 strings in the list with the anwser key has ended since, at the very least, you can't keep comparing "floweR" in "flows"
# "flower" "flows"
#  012345   01234
#       i    12345
#remember that the longest common prefix must apply to ALL 3 STRINGS - we are only as strong as our weakest or shortest member in this case

#you have to use indexes aka i to compare to len(s) comparing len with len has the possibility to run into an index out of bounds error because, in the process of comparing, you're trying to access an index that is not valid in the other
#you have to use len(s) because s isn't accessed with i and range while strs 
                
#4/6/24 review: (missed): the key missed insight is to use the 1st string in the array as a comparing point for all other strings since all have to match!

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

#practice again:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])): #only 1st string
            for s in strs: #each string
                #if we reached the end of our string we are iterating over or anypoint dosen't match
                if i == len(s) or s[i] != strs[0][i]: #because strs[0] represents the 1st string in our input list, and that comparison stays permernant. the i part keeps moving to compare the same character in the 0th index string (permernant) and our current string's character out of all strings in input (s[i])
                    return res
            res += strs[0][i]
        return res 

#4/7/24:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

#4/8/24:

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])): #use strs[0] as comparision key since all strings in strs input list have to match to count towards res string
            for s in strs: #each string in the list that moves
                if i == len(s) or s[i] != strs[0][i]: #found violating condition, so return: already reached end of current string we are iterating over or there is a mismatch somewhere with the strs[0] key using the ith position in the one we are iterating over and the key
                    return res
            #once we have looped through that entire string, we can add the anwser up to this point - matching string - to result, which is going to be a portion of the strs[0] key string since that is never changing
            res += strs[0][i]
        return res #once we finis iterating over each string in strs input list and also finished iterating over each character in strs[0] key string, we can determine out result since every string has to match up in strs list input


#4/9/24 refresher:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

#4/26/24 refresher:

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

#5/21/24 practice:

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for words in strs:
                if i >= len(words) or words[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

#6/17/24 review (my own solution in python3):

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or strs[0][i] != word[i]:
                    return res
            res += strs[0][i]
        return res

#7/17/24 review (my own solution):

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for char in strs[1:]:
                if i >= len(char) or char[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
