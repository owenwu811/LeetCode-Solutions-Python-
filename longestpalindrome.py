#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



#s = "abccccdd" > output is 7 because "dccaccd" 

#note that we can rearrange the letters of the input however we would like to make palindrome!!!

#python3 solution:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for char in s:
            if char not in seen: #odd occurence means add
                seen.add(char)
            else: #even occurence means remove
                seen.remove(char)
        return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)


#the idea here is that only one of the odd frequency characters from the input can be tolerated as we can just plop it in the middle, so rest of how ever many odd characters need to be subtracted from the length of input string
#to illustrate, abccccdd > 1 a, 1 b, 4 cs, 2 ds, so we can either choose a OR b to plop in the middle, and the other odd has to be removed from input
# aaabccccdd > 3 as, 1 b, 4 cs, 2 ds, so, again we can chose ONE OF THE 3 AS or JUST THE B to plop in the middle, and the all the other odds (2 a + 1 b or 3 a) need to be removed from input
# dccaccd, so we are left with aab in the input, and no matter how you put aab inside of dccaccd, you will never form a palindrome - if you put the 2 as in front and the b in middle, you get adccbaccda or adccabccda, which are not palindromes because the b gets hit first or later when coming backwards vs. forwards, so you gotta remove 3 (aab or aaa) as length from input since we already tolerated one of the odds - 4 total - aaab = len(4), and we either removed ONE a or ONE b 


#for "aaaccccdd", res is 9 (whole input) because you can do adccaccda, so the set is {'a'} at the end, and since we can tolerate one of the As by adding 1, we can plop the other 2 As at end, so we can tolerate one of the 3 As

#no matter how long that odd character is, we can count the entire input string if we only have one odd letter, so if we have 5 As, as long as we only have one unique odd character, then we can count the entire stirng as palindrome length




#if you had 7 as, #aaaaaaaccccdd - you could still get the entire thing with - #aaaddccaccddaaa


#4/28/24 refresher:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        seen = set()
        for char in s:
            if char not in seen: #odd
                seen.add(char)
            else:
                seen.remove(char)
        return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)

#4/29/24:

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        for char in s:
            if char not in seen: #odd
                seen.add(char)
            else:
                seen.remove(char) #even
        #seen contains one occurence of all letters that appeared an odd number of times
        return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)

#4/30/24 refresher:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for char in s:
            if char not in seen: #odd
                seen.add(char)
            else:
                seen.remove(char) #even
        #we can tolerate one of the characters that appeared an odd number of times in input string 
        return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)

#5/3/24 refresher:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                seen.remove(char)
        return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)

#5/15/24 refresher:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for i in s:
            if i not in seen: #odd
                seen.add(i)
            else:
                seen.remove(i)
        return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)

#5/26/24 review:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        seen = set()
        for char in s:
            if char not in seen: #odd
                seen.add(char)
            else: #even
                seen.remove(char)
        return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)

#6/24/24 review:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 1
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                seen.remove(char)
                res += 1
        return len(s) - len(seen) + 1 if len(seen) > 1 else len(s)



#7/11/24 review:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                seen.remove(char)
        return len(s) - len(seen) + 1 if seen else len(s)

