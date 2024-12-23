#Given a string s, find the length of the longest 
#substring
# without repeating characters.


#Example 1:

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:

#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

#Constraints:

#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.


#brute force solution that gets TLE 986/897:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1] 
                if len(substr) == len(set(substr)):
                    res = max(res, len(substr))
        return res



#My Solution:

class Solution:
    import math
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicatecheck = set() #we use a set data structure to check if the element that windowend is pointing to, aka we are about to add, is a duplicate or not
        windowstart = 0 
        windowend = 0
        length = 0 #we set length to 0 so that any length that comes after it will be bigger 
        for windowend in range(len(s)): #we are expanding the window with the windowend pointer
            while s[windowend] in duplicatecheck: #if we find a duplicate, we keep shrinking the window until we don't have anymore duplicates
                duplicatecheck.remove(s[windowstart]) #if the windowend pointer we are about to add is already in the set, shrink the window by removing 
                windowstart += 1 #we are shrinking the window with the left pointer, which is windowstart
            duplicatecheck.add(s[windowend]) #if we don't have this, we can't use line 9 to determine if it's a duplicate or not because we're checking to see if it already exists in the set to determine if we need to shrink the window
            length = max(length, windowend - windowstart + 1) #update the maximum length of the valid window
        return length #after we finished trasversing our entire array, we return the max length we found that consists of unique characters
  
   #THINK OF LINE 41 AS A TALLY SYSTEM OF DUPLICATE ALLOWANCES: we do this so that when we check the set in the future for the same character, we know we already removed it once and so it can be duplicated once. 
   #in line 44, we are comparing the history's greatest window up to that point with the current window, not 0 with the current window even though 38 is length because length gets updated with the bigger of the two between the history's biggest and the current in line 44.
   #line 44 returns to line 39, and the for loop in line 39 automatically increments and expands our window. 
   #for windowend in range(len(s)) goes up to but not including the length of the array, which is the index because index is always one less than the length. This is denoted by the range function
   # you cannot use an if statement in line 40 because it would shrink the window once and still proceed to add the right pointer character without continuing to check if the duplicates have been removed
   
#Another Solution:

class Solution:
    import math
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowstart, result, duplicatecheck = 0, 0, set()
        #we use a set, not a dictionary, to check for duplicates
        for windowend in range(len(s)):
            while s[windowend] in duplicatecheck: #if there is a duplicate
                duplicatecheck.remove(s[windowstart])
                windowstart += 1
            result = max(result, windowend - windowstart + 1) #note that it dosen't matter if we check the result and then add windowend or add windowend and then check the length as long as the current character (windowend) is added so that we make sure the current windowend's character only appears once in the set and is not a duplicate
            duplicatecheck.add(s[windowend]) #lines 65 and 66 can be swapped in terms of order
        return result
        
        
 #Refresher 5/18/23:
 
 class Solution:
    import math
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthoflongest, windowstart, duplicatecheck = 0, 0, set()
        for windowend in range(len(s)):
            while s[windowend] in duplicatecheck:
                duplicatecheck.remove(s[windowstart]) #make changes to set first so we keep the tally system in check
                windowstart += 1 #shrink window
            duplicatecheck.add(s[windowend]) #no more duplicates, so add windowend since, if windowend was a duplicate, that tally was removed by windowstart because windowstart must be a character that windowend was already on, which means windowstart and windowend are the same thing at some point if windowend is a duplicate
            lengthoflongest = max(lengthoflongest, windowend - windowstart + 1)
        return lengthoflongest

#Refresher 8/1/23:

class Solution:
    import math
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthoflongest, duplicatecheck, windowstart = 0, set(), 0
        for windowend in range(len(s)):
            while s[windowend] in duplicatecheck: #this must be a while and not an if statement because we need to continually shrink the window when the next character is a duplicate from the windowstart side
                duplicatecheck.remove(s[windowstart])
                windowstart += 1
            duplicatecheck.add(s[windowend])
            lengthoflongest = max(lengthoflongest, windowend - windowstart + 1)
        return lengthoflongest

#Refresher 9/23/23:

class Solution:
    import math
    def lengthOfLongestSubstring(self, s: str) -> int:
        historicalbiggest = 0
        duplicatecheck = set()
        windowstart = 0
        for windowend in range(len(s)):
            while s[windowend] in duplicatecheck: #while is used because if there is more than 1 duplicate, we have to keep removing the duplicate with windowstart until no duplicates are left, not just remove 1 of the duplicates aka the tally system has to even out
                duplicatecheck.remove(s[windowstart]) #you have to keep shrinking the window USING WINDOWSTART until you get rid of both w's if there are 2 ws and then when there are no duplicates, then you can add the windowend character and start counting the new window as a potential new window length result
                windowstart += 1
            duplicatecheck.add(s[windowend])
            currentwindowlength = windowend - windowstart + 1
            historicalbiggest = max(historicalbiggest, currentwindowlength)
        return historicalbiggest

#12/18/2023 refresher solution:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        repeatingcheck = set()
        l = 0
        for r in range(len(s)):
            while s[r] in repeatingcheck:
                repeatingcheck.remove(s[l])
                l += 1
            repeatingcheck.add(s[r])
            res = max(res, len(repeatingcheck)) #note that len(set) works here too instead of just we - ws + 1 since both are the same mechanism 
        return res


#12/25/23 refresher solution:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        duplicatecheck = set()
        res = 0
        ws = 0
        for we in range(len(s)):
            while s[we] in duplicatecheck:
                duplicatecheck.remove(s[ws])
                ws += 1
            duplicatecheck.add(s[we])
            res = max(res, len(duplicatecheck))
        return res


#1/8/24 refresher solution:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        duplicatecheck = set()
        ws = 0
        for we in range(len(s)):
            while s[we] in duplicatecheck:
                duplicatecheck.remove(s[ws])
                ws += 1
            duplicatecheck.add(s[we])
            res = max(res, len(duplicatecheck))
        return res



#1/28/24 refresher:

#we want to length of the longest substring without repeating characters, so our return type will be an integer
        res = 0
        #without repeating characters means we want a set to keep track of what we already have seen while looping through s
        dc = set()
        #we will slide the window, expanding and shrinking depending on if we have seen the character already or not - if we've already seen the current character we are seeing with windowend pointer, we keep shrinking the window from the beginning to not duplicate calculate windows that we have already calculated. 
        ws = 0
        for we in range(len(s)):
            while s[we] in dc:
                dc.remove(s[ws])
                ws += 1
            dc.add(s[we])
            res = max(res, len(dc))
        return res


#2/4/24 refresher solution:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #we want the length as an integer
        res = 0
        #no repeating characters - we will use a set to keep track of the longest possible window
        dc = set()
        ws = 0
        for we in range(len(s)):
            while s[we] in dc:
                #we want to kickout from left accurately, so this comes before ws += 1 because don't want to alter the one we will use to see which one to kick out before we actually kick it out
                dc.remove(s[ws])
                ws += 1
            dc.add(s[we])
            res = max(res, len(dc))
        return res

#2/20/24:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        dc = set()
        ws = 0
        for we in range(len(s)):
            while s[we] in dc:
                dc.remove(s[ws])
                ws += 1
            dc.add(s[we])
            res = max(res, len(dc))
        return res


#3/23/24:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        ws = 0
        seen = set()
        for we in range(len(s)):
            while s[we] in seen:
                seen.remove(s[ws])
                ws += 1
            seen.add(s[we])
            res = max(res, len(seen))
        return res

#4/21/24 refresher:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        ws = 0
        for we in range(len(s)):
            while s[we] in seen:
                seen.remove(s[ws])
                ws += 1
            seen.add(s[we])
            res = max(res, len(seen))
        return res


#5/17/24 practice:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lengthoflongest = 0
        seen = set()
        ws = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[ws])
                ws += 1
            seen.add(s[i])
            lengthoflongest = max(lengthoflongest, i - ws + 1)
        return lengthoflongest


#6/12/24 review:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        ws = 0
        seen = set()
        for we in range(len(s)):
            while s[we] in seen:
                seen.remove(s[ws])
                ws += 1
            seen.add(s[we])
            res = max(res, len(seen))
        return res


#7/14/24 refresher:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lengthoflongest = 0
        seen = set()
        ws = 0
        for we in range(len(s)):
            while s[we] in seen:
                seen.remove(s[ws]) #we remove the char we are kicking out of the window since sets are unordered in python - this letter is identified by s[ws] as ws and we represent the boundaries of our current window
                ws += 1
            seen.add(s[we])
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest

#9/17/24 review:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        myset = set()
        l = 0
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            res = max(res, len(myset))
        return res


#10/31/24 review:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        myset = set()
        for r in range(len(s)):
            while myset and s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            res = max(res, len(myset))
        return res



#12/19/24 review:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            res = max(res, len(seen))
        return res

