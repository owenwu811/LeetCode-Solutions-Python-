
#1415

#A happy string is a string that:

#consists only of letters of the set ['a', 'b', 'c'].
#s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
#For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

#Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

#Return the kth string of this list or return an empty string if there are less than k happy strings of length n.



#correct python3 solution: (could not solve by myself and need to review later):

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = []
        self.pool = "abc"
        def f(cur):
            if len(cur) == n:
                self.res.append(cur)
                return
            for char in self.pool:
                #either cur is empty meaning there is no previous character to cause duplicates or cur is not empty and the current char we are trying to add is not the same as the last character at the rear of cur
                if len(cur) == 0 or char != cur[-1]:
                    f(cur + char)
        f("")
        if len(self.res) < k: return ""
        return self.res[k - 1]
