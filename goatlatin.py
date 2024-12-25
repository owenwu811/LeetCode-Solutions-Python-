#824
#easy

#You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

#We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

#If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
#For example, the word "apple" becomes "applema".
#If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
#For example, the word "goat" becomes "oatgma".
#Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
#Return the final sentence representing the conversion from sentence to Goat Latin.

 

#Example 1:

#Input: sentence = "I speak Goat Latin"
#Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


#my own solution using python3:

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new = sentence.split(" ")
        print(new)
        res = []
        for i, n in enumerate(new):
            if n[0].lower() in "aeiou":
                now = n + "ma"
                cur = i + 1
                while cur > 0:
                    now += "a"
                    cur -= 1
                res.append(now)
            else:
                newstr = n[1:] + n[0]
                newstr += "ma"
                cur = i + 1
                while cur > 0:
                    newstr += "a" 
                    cur -= 1
                res.append(newstr)
        return " ".join(res)
