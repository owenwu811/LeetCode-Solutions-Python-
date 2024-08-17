#medium
#720


#python3 solution:

#words.sort() turns ["a", "banana", "app", "appl", "ap", "apply", "apple"] into ['a', 'ap', 'app', 'appl', 'apple', 'apply', 'banana'] so basically alphabetical order and also apple apply 

#Word[:-1] is different from word[::-1]!
#Longest Word in Dictionary - this solution should be reviewed since it’s somewhat intuitive!

#Given an array of strings words representing an English Dictionary, return the longest word in wordsthat can be built one character at a time by other words in words.
#If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
#Note that the word should be built from left to right with each additional character being added to the end of a previous word. 
 
#Example 1:
#Input: words = ["w","wo","wor","worl","world"]
#Output: "world"
#Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

#Example 2:
#Input: words = ["a","banana","app","appl","ap","apply","apple"]
#Output: "apple"
#Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

class Solution:
   def longestWord(self, words: List[str]) -> str:
       words.sort()                  # for smallest lexicographical order
       visited = {""}                # hashset to keep a track of visited words
       res = ''
      
       for word in words:
           if word[:-1] in visited:     # check previous word ie. word[:len(word)-1] visited or not
               visited.add(word)        # add this word to the set
               if len(word) > len(res): # current word have greater lenght and lexicographically smaller
                   res = word           # update res
      
       return res
  
#note that word[:-1] is “app” > “ap” - up to not including the final one! Aka means the previous word in visited or not
