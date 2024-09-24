
#1433
#medium

#Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

#A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

 


#correct python3 solution (could not solve):

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        f, s = sorted(s1), sorted(s2)
        print(f)
        print(s)
        flag = True
        for i in range(len(f)):
            if f[i] >= s[i]:
                continue
            else:
                flag = False
        for i in range(len(s)):
            if s[i] >= f[i]:
                continue
            elif not flag:
                return False
        return True
