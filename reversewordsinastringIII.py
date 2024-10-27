
#557
#easy

#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

#Example 1:

#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
#Example 2:

#Input: s = "Mr Ding"
#Output: "rM gniD"


#my own solution using python3:

class Solution:
    def reverseWords(self, s: str) -> str:
        myl = s.split(" ")
        print(myl)
        for i, l in enumerate(myl):
            myl[i] = l[::-1]
        print(myl)
        res = ""
        for i, l in enumerate(myl):
            res += l
            if i < len(myl) - 1:
                res += " "
        return res
