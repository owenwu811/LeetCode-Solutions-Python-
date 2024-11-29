
#2129
#easy

#You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

#If the length of the word is 1 or 2 letters, change all letters to lowercase.
#Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
#Return the capitalized title.

 

#Example 1:

#Input: title = "capiTalIze tHe titLe"
#Output: "Capitalize The Title"
#Explanation:
#Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.


#my own solution using python3:

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t = title.split(" ")
        print(t)
        new = []
        for word in t:
            if len(word) == 1 or len(word) == 2:
                new.append(word.lower())
            else:
                print(word[0].upper())
                cur = ""
                cur += word[0].upper() 
                cur += word[1:].lower()
                print(cur)
                new.append(cur)
        return " ".join(new)
