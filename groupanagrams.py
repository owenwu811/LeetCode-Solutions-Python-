
#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


#Example 1:

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]



#Python3 solution:

class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       strs_table = {}
       for string in strs:
           #''.join() operation is necessary to ensure that sorted_string is a hashable string, which can be used as a dictionary key. Without .join(), sorted_string becomes a list of characters, which cannot be used as a dictionary key.
           #sorted_string = sorted(string) - results in a LIST of characters
           #strs_table[sorted_string].append(string) - You are trying to use a list (sorted_string) as a dictionary key, which is not allowed because lists are mutable, and mutable objects cannot be dictionary keys.


#In contrast, in the original code with .join(), you were creating a sorted string representation like this: sorted_string = ''.join(sorted(string)) - The result of this operation is a string. For example, if string is "listen," then sorted_string will be "eilnst," which is a string.


#Because sorted_string is a string in this case, you can use it as a dictionary key without any issues because strings are hashable in Python.
           sorted_string = ''.join(sorted(string)) #we are taking the string, sorting it, and using the sorted version of the string as a dictionary key
           if sorted_string not in strs_table: #if the dictionary key dosen't yet exist, then create it, and then add it to it's own list
               strs_table[sorted_string] = []
           strs_table[sorted_string].append(string) #the sorted version of the string already exists as a dictionary key, so append it to the appropriate list
       return list(strs_table.values()) #return the resulting values of the dictionary because the key represents the sorted/processed judge version to be compared to while we want to return the original, unsorted version of the string that matches the judge after it's sorted
          


           # if string is "listen," then sorted(string) will result in ['e', 'i', 'l', 'n', 's', 't'], which is a LIST
           #''.join(sorted(string)) takes the list of sorted characters and joins them together into a single string with no whitespace. For example, if string is "listen," then ''.join(sorted(string)) will result in the string "eilnst."
