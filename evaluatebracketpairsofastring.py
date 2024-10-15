

#1807
#medium

#You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

#For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
#You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

#You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:

#Replace keyi and the bracket pair with the key's corresponding valuei.
#If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
#Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

#Return the resulting string after evaluating all of the bracket pairs.


#correct python3 solution (my own solution after looking at another solution):


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict()
        for k in knowledge:
            if k[0] not in d:
                d[k[0]] = k[1]
        i = 0
        cur = ""
        tmp = ""
        while i < len(s):
            if s[i] == "(":
                i += 1
                while s[i] != ")":
                    cur += s[i]
                    i += 1
                print(cur)
                if cur in d:
                    tmp += d[cur]
                else:
                    tmp += "?"
                cur = ""
            else:
                tmp += s[i]
            i += 1
        return tmp
