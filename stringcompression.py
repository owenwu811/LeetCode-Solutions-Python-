#443
#medium


#Given an array of characters chars, compress it using the following algorithm:

#Begin with an empty string s. For each group of consecutive repeating characters in chars:

#If the group's length is 1, append the character to s.
#Otherwise, append the character followed by the group's length.
#The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

#After you are done modifying the input array, return the new length of the array.

#You must write an algorithm that uses only constant extra space.

 

#Example 1:

#Input: chars = ["a","a","b","b","c","c","c"]
#Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
#Example 2:

#Input: chars = ["a"]
#Output: Return 1, and the first character of the input array should be: ["a"]
#Explanation: The only group is "a", which remains uncompressed since it's a single character.
#Example 3:

#Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
#Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

#correct python3 solution:

class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0  # To keep track of the position in the original list
        i = 0  # To iterate through the list

        while i < len(chars):
            char = chars[i]
            count = 0 #notice count resets to 0 after each time i moves up to the next first different letter like from a to b 
            for j in range(i, len(chars)): #notice j starts exactly on i as shown in kevin's video drawing
                if chars[j] == char:
                    count += 1 #keeping track of the count of the character as long as j and i are seeing the same character
                else:
                    break #j is on a different character now, like b, so break because we found the end of a sequence 

            chars[index] = char 
            index += 1 #index never resets to 0 like with count

            if count > 1: #only if the frequency of the letter appeared more than once is it worth it because it will make it shorter like aaa is longer than a3
                for digit in str(count): #count = 2, so digit has one iteration where it equals "2"
                    chars[index] = digit #turning ['a', 'a'] into ['a', '2'] and then ['b', 'b'] into ['b', '2']
                    index += 1

            i += count #i has to move up to the next letter b , so i goes from 0 to 2

        return index
