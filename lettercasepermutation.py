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
                f(i + 1, cur + S[i]) #after we find out first result of "a1b2", we backtrack by popping off, so we now have "a1b", and then we backtrack again to "a1" before calling - f(i + 1, cur + S[i].upper()) - which then results in "a1B", and then we call this else block again to get "a1B2", and then we hit our base case, and our res looks like ["a1b2","a1B2"] now, and then we backtrack from "a1B2" all the way back to "" because the only path we haven't explored is starting where the a in "a1B2" isn't capitalized, so call - f(i + 1, cur + S[i].upper()) - which results in "A", next, we see a 1, so call the else block, which results in "A1". next, we call - f(i + 1, cur + S[i].lower()) - which results in "A1b" - notice the b as lowercase because we have to try lowercase combos before upper hence why the lower recursive call is placed before the upper one. Next, we call the else block, which results in "A1b2", so we hit our base case, and result = ["a1b2",	"a1B2",	"A1b2"].... 

        f(0, "")
        return res
