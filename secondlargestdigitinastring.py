

#easy
#50.7%acceptancerate
#1796

#Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

#An alphanumeric string is a string consisting of lowercase English letters and digits.

 

#Example 1:

#Input: s = "dfa12321afd"
#Output: 2
#Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
#Example 2:

#Input: s = "abc1111"
#Output: -1
#Explanation: The digits that appear in s are [1]. There is no second largest digit. 


#my own solution using python3:

class Solution:
    def secondHighest(self, s: str) -> int:
        key = "0123456789"
        a = []
        for char in s:
            a.append(char)
        #print(a)
        r = []
        for c in a:
            if c in key:
                r.append(int(c))
        print(r)
        myset = set()
        for a in r:
            if a not in myset:
                myset.add(a)
        res = []
        for s in myset:
            res.append(s)
        res.sort(reverse=True)
        print(res)
        return res[1] if len(res) >= 2 else -1
            
