#easy
#83.3% acceptance rate


#A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

#A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

#For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
#Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

 

#Example 1:

#Input: s = "is2 sentence4 This1 a3"
#Output: "This is a sentence"
#Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.



#my own solution using python3:

class Solution:
    def sortSentence(self, s: str) -> str:
        d = dict()
        l = s.split(" ")
        print(l)
        for word in l:
            if word not in d:
                d[word[-1]] = word[:-1]
        print(d)
        sortd = dict(sorted(d.items(), key=lambda item:item[0]))
        print(sortd)
        res = ""
        for k in sortd:
            res += sortd[k]
            res += " "
        return res.rstrip()
