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
        maxlength = 0
        windowstart = 0
        char_freq = {}
        max_char_freq = 0
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
        result = 0
        charfrequency = {}
        windowstart = 0
        maxcharacter = 0
        for windowend in range(len(s)):
            if s[windowend] not in charfrequency:
                charfrequency[s[windowend]] = 0
            charfrequency[s[windowend]] += 1
            maxcharacter = max(maxcharacter, charfrequency[s[windowend]]) # we find the biggest value out of keys for each new iteration
            if (windowend - windowstart + 1) - maxcharacter > k: #if we do not have enough flips, as denoted by k, then we execute this inner block to shrink the window and reflect the same changes in our dictionary
                leftchar = s[windowstart]
                charfrequency[leftchar] -= 1
                windowstart += 1
            result = max(result, windowend - windowstart + 1) #if we do have enough flips, as denoted by k, return the length of the window. the question just asks if the flips are possible and to find the longest substring that is possible with the k limitatino. The question never asks to count the number of flips to get each substring.
        return result
