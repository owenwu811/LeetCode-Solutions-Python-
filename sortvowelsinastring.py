
#medium
#81.3%acceptancerate

#Given a 0-indexed string s, permute s to get a new string t such that:

#All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
#The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
#Return the resulting string.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.
 

#Example 1:

#Input: s = "lEetcOde"
#Output: "lEOtcede"
#Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.


#my own solution using python3 after looking at hints:

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aAeEiIoOuU'
        tmp = []
        where = []
        for i, char in enumerate(s):
            if char in vowels:
                where.append(i)
                tmp.append(char)
        tmp.sort()
        print(tmp)
        print(where)
        #mydict = dict()

        #for char in s:
        #    for t in tmp:
        #        if char in vowels:
        #            s = s.replace(char, t, 1)
        #print(s)
        #arr = []
        #for i in range(len(s)):
        #    if i in where:
        #        arr[i] = tmp[i]
        #    else:
        #        arr[i] = s[i]
        #print(arr)
        arr = []
        for i, char in enumerate(s):
            if char in vowels:
                continue
            else:
                arr.append(char)
        print(arr)
        for i, w in enumerate(where):
            arr.insert(w, tmp[i])
        return "".join(arr)

        
