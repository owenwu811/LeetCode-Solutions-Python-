

#186
#medium


#Given a character array s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

#Your code must solve the problem in-place, i.e. without allocating extra space.

 

#Example 1:

#Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
#Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
#Example 2:

#Input: s = ["a"]
#Output: ["a"]




#my own solution using python3:

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == s[::-1] or len(s) == 2:
            return s
        orig = s.copy()
        l, r = 0, len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        marker = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[marker: i + 1] = s[marker: i + 1][::-1]
                marker = i + 1
        print(s)
        for i in range(len(s)):
            if i >= 0 and i < len(s):
                if s[i] == " " and i == 0:
                    s.remove(s[i])
        print(s)
        print(orig)
        j = 0
        for i in range(len(orig)):
            if orig[i] == " ":
                j = i
                break
        print(j)
        print(s[-j:])
        s[-j:] = s[-j:][::-1]
        print(s)
        s.insert(-j, " ")
        print(s)
