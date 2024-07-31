#Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

#Return a list of all possible strings we could create. Return the output in any order.

#Input: s = "a1b2"
#Output: ["a1b2","a1B2","A1b2","A1B2"]


#bactracking pattern


#Python3 solution:

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def f(i, cur):
            if i >= len(S):
                res.append(cur)
                return
            if S[i].isalpha(): 
                f(i + 1, cur + S[i].lower()) #keep trying all the lowercase variations before trying upper and then lower
                f(i + 1, cur + S[i].upper())
            else: #if we see a number, then just add the number because numbers don't have upper or lower case
                f(i + 1, cur + S[i])

        f(0, "")
        return res
