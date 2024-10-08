
#medium
#3271

#You are given a string s of length n and an integer k, where n is a multiple of k. Your task is to hash the string s into a new string called result, which has a length of n / k.

#First, divide s into n / k 
#substrings
#, each with a length of k. Then, initialize result as an empty string.

#For each substring in order from the beginning:

#The hash value of a character is the index of that character in the English alphabet (e.g., 'a' → 0, 'b' → 1, ..., 'z' → 25).
#Calculate the sum of all the hash values of the characters in the substring.
#Find the remainder of this sum when divided by 26, which is called hashedChar.
#Identify the character in the English lowercase alphabet that corresponds to hashedChar.
#Append that character to the end of result.
#Return result.

 

#Example 1:

#Input: s = "abcd", k = 2

#Output: "bf"

#Explanation:

#First substring: "ab", 0 + 1 = 1, 1 % 26 = 1, result[0] = 'b'.

#Second substring: "cd", 2 + 3 = 5, 5 % 26 = 5, result[1] = 'f'.



#my own solution using python3:

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        alpha = "abcdefghijklmnoqrstuvwxyz"
        d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 
        'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 
        'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        for i in range(0, len(s), k):
            cursum = 0
            print(type(i))
            print(type(k))
            window = s[i: i + k]
            #window = s[int(i): int(i) + int(k)]
            for w in window:
                cursum += d[w]
            remainder = cursum % 26
            print(remainder)
            for j in d:
                if d[j] == remainder:
                    res += j
        return res
            
