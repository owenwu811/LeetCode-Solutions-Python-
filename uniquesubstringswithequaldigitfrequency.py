

#2168
#medium

#Given a digit string s, return the number of unique substrings of s where every digit appears the same number of times.
 

#Example 1:

#Input: s = "1212"
#Output: 5
#Explanation: The substrings that meet the requirements are "1", "2", "12", "21", "1212".
#Note that although the substring "12" appears twice, it is only counted once.
#Example 2:

#Input: s = "12321"
#Output: 9
#Explanation: The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".



#my own solution after making a little change from someone else's solution:

class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        c = Counter()
        myset = set()
        for i in range(len(s)):
            c.clear()
            for j in range(i, len(s)):
                c[s[j]] += 1
                if len(set(c.values())) == 1:
                    print(c)
                    myset.add(s[i: j + 1]) #add the entire substring! not just the keys of counter!
        print(myset)
        
        return len(myset)
