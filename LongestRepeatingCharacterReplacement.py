You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length


My Solution:
  
  class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        maxlength, windowstart, max_char_freq = 0, 0, 0
        char_freq = {}
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_freq:
                char_freq[right_char] = 0
            char_freq[right_char] += 1
            max_char_freq = max(max_char_freq, char_freq[right_char])
            currlength = window_end - windowstart + 1
            if currlength - max_char_freq > k: #represents the number of characters in current substring that aren't most frequently occuring 
            #and the reason we want the not most frequently occuring is because it always makes sense to flip the character with less number of flips to make everything equal
                #if the number is bigger than k, we have to change more than k characters to get a valid substring consisting of only a single character, so shrink the window by moving windowstart to the right
                left_char = s[windowstart]
                char_freq[left_char] -= 1 #when we shrink the window, we have to reflect that change in our dictionary
                windowstart += 1
            maxlength = max(maxlength, window_end - windowstart + 1)
        return maxlength
#shrinking the window is only used to fufill the k condition

            
#max_char_freq is the frequency of most frequently occuring character in current window while max_len is the length of the longest substring with same character seen so far 
            
 #Clarifications: The problem description doesn't explicitly state that the input string consists of only two different letters. 
 # However, this can be inferred from the problem statement, which asks for the length of the longest substring containing the same letter after performing at most k character replacements. 
 # Since there are only two different letters in the string, we can only perform character replacements between those two letters, which means that the resulting substring will also only contain those two letters.

 
 #My other solution:
 #I find this even more intuitive than my first solution as you don't need to worry about rightchar = s[windowend] being placed after if s[windowend] not in charfrequency, which would ask if the previous iteration's windowend character is in the dictionary, not the current iterations because the association - rightchar = s[windowend] must happen before the if check to be valid. 
 
 class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        result, windowstart, maxcharacter = 0, 0, 0 #result is what we will return in the end while maxcharacter gets updated on each turn
        charfrequency = {}
        for windowend in range(len(s)):
            if s[windowend] not in charfrequency: 
                charfrequency[s[windowend]] = 0 #only executes to create a new row for a char that dosen't already exist in the dictionary
            charfrequency[s[windowend]] += 1
            maxcharacter = max(maxcharacter, charfrequency[s[windowend]]) # we find the biggest value out of keys for each new iteration
            if (windowend - windowstart + 1) - maxcharacter > k: #if we do not have enough flips, as denoted by k, then we execute this inner block to shrink the window and reflect the same changes in our dictionary
                leftchar = s[windowstart]
                charfrequency[leftchar] -= 1
                windowstart += 1
            result = max(result, windowend - windowstart + 1) #if we do have enough flips, as denoted by k, return the length of the window. the question just asks if the flips are possible and to find the longest substring that is possible with the k limitatino. The question never asks to count the number of flips to get each substring.
        return result
       
#In line 76, we can either subtract the current window's length by the highest frequency value in the dictionary or lowest frequency value. It would make sense to subtract by the highest frequency value to minimize the number of flips to maximize the chances of satisfying k. Again, the purpose here is solely to find the number of changes to get the entire string to be of one character assuming that the entire string only consists of two characters to begin with.
#[......III] 
#[xxxxxxxxx] > should we subtract the . or III from x? Probably III as that would result in less flips for k
# xxxxxxxxx - III = 6. If 6 > k, we have a problem. Otherwise, we can go ahead and say 6 is a valid canditate for our result.


7/1/23 refresher (my solution):

class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {} #keeping track of frequency of characters
        windowstart, mostfrequent, lengthoflongest = 0, 0, 0 #integers representing indicies 
        lengthoflongest variable will be our anwser at the end
        for windowend in range(len(s)):
            if s[windowend] not in frequency:
                frequency[s[windowend]] = 0
            frequency[s[windowend]] += 1
            mostfrequent = max(mostfrequent, frequency[s[windowend]])
            if (windowend - windowstart + 1) - mostfrequent > k: #don't have enough flips to make the same letters in a row, so shrink the window
                frequency[s[windowstart]] -= 1 #don't need a refrence to windowstart right above this line since it's already defined in line 95.
                windowstart += 1
            else:
                lengthoflongest = max(lengthoflongest, windowend - windowstart + 1) #length, not indicies, so + 1
        return lengthoflongest


#3/26/24 refresher (missed):

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #you can replace at most k times
        frequency = {}
        lengthoflongest, mostfrequent, ws = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - ws + 1) - mostfrequent > k:
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest
         


#3/26/24 practice again:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        lengthoflongest, ws, mostfrequent = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - ws + 1) - mostfrequent > k:
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest

#3/27/24:

class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        lengthoflongest, mostfrequent, ws = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - ws + 1) - mostfrequent > k: #it seems like we aren't limited to only flipping letters in a particular order - we can flip anywhere as long as the number of flips is less or equal to k
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1) 
        return lengthoflongest


#3/27/24:

class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        #at most k times 
        frequency = {}
        lengthoflongest, mostfrequent, ws = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - ws + 1) - mostfrequent > k:
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest


#3/29/24:

class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        lengthoflongest, mostfrequent, ws = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - ws + 1) - mostfrequent > k:
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest

#3/31/24:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        lengthoflongest, mostfrequent, ws = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - ws + 1) - mostfrequent > k:
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest

#4/4/24:

class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        lengthoflongest, windowstart, mostfrequent = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - windowstart + 1) - mostfrequent > k:
                frequency[s[windowstart]] -= 1
                windowstart += 1
            lengthoflongest = max(lengthoflongest, we - windowstart + 1)
        return lengthoflongest

#4/6/24:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        lengthoflongest, ws, mostfrequent = 0, 0, 0
        for i in range(len(s)):
            if s[i] not in frequency:
                frequency[s[i]] = 0
            frequency[s[i]] += 1
            mostfrequent = max(mostfrequent, frequency[s[i]])
            while (i - ws) + 1 - mostfrequent > k:
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, i - ws + 1)
        return lengthoflongest
            
#4/9/24:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        lengthoflongest, ws, mostfrequent = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in freq:
                freq[s[we]] = 0
            freq[s[we]] += 1
            mostfrequent = max(mostfrequent, freq[s[we]]) # we want least work for k since k is limited
            while (we - ws + 1) - mostfrequent > k:
                freq[s[ws]] -= 1
                ws += 1
            #k is satisfied
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest


#4/20/24:

class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        lengthoflongest, ws, mostfrequent = 0, 0, 0 #mostfrequent puts the least strain on k, which is our limiting constraint 
        for i in range(len(s)):
            if s[i] not in frequency:
                frequency[s[i]] = 0
            frequency[s[i]] += 1
            mostfrequent = max(mostfrequent, frequency[s[i]]) #after we discover a new character, we could have a new mostfrequent character, which we do on the 1st iteration
            while (i - ws + 1) - mostfrequent > k: 
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, i - ws + 1)
        return lengthoflongest

#4/24/24:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we want to minimize the number of times we have to use k
        freq = dict()
        lengthoflongest, ws, mostfrequent = 0, 0, 0
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 0
            freq[s[i]] += 1
            #if we find the mostfrequent letter, and we subtract our window by the mostfrequent, then that's the least work for k
            mostfrequent = max(mostfrequent, freq[s[i]])
            while (i - ws + 1) - mostfrequent > k:
                freq[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, i - ws + 1)
        return lengthoflongest


#5/4/24 refresher:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        mostfrequent, lengthoflongest, ws = 0, 0, 0
        for we in range(len(s)):
            if s[we] not in frequency:
                frequency[s[we]] = 0
            frequency[s[we]] += 1
            mostfrequent = max(mostfrequent, frequency[s[we]])
            while (we - ws + 1) - mostfrequent > k:
                frequency[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest


#5/23/24:

class Solution:
    import math
    def characterReplacement(self, s: str, k: int) -> int:
        lengthoflongest, ws, mydict, mostfrequent = 0, 0, dict(), 0
        for we in range(len(s)):
            if s[we] not in mydict:
                mydict[s[we]] = 0
            mydict[s[we]] += 1
            mostfrequent = max(mostfrequent, mydict[s[we]])
            while (we - ws + 1) - mostfrequent > k:
                mydict[s[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)
        return lengthoflongest



