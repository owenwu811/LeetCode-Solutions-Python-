#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]



#python3 solution:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        def myfunc(result):
            #since we want "ad", "ae"... we want to make sure that the length of our result path - "ad" is equal to the length of our input - digits - "23" - both have to be 2 for us to hit our base case and for result = "a" and letterlistr = "d" to change to result = "a" and letterlistr = "e"
            if len(result) == len(digits):
                res.append(result)
            #the idea is that, without this else and indenting for loop, we will get index out of bounds error because we won't reset letterlistr after hitting the base case
            else:
                #mapping is the dictionary, so if len(result) == 0 since result = "", then digits[0] = 2 given the input digits = "23", so then mapping[2] corresponds to the first k, v pair - '2': ['a', 'b', 'c'], and letterlistr will take on 'a'
                for letterlistr in mapping[digits[len(result)]]:
                    myfunc(result + letterlistr)
        myfunc("")
        return res
        

#after "af" gets appended to res list, letterlistr goes from "a" > "b" and result goes from "af" > ""


#refresher:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return []
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        def myfunc(path):
            if len(digits) == len(path):
                res.append(path)
            else:
                #for letter in mapping[2] if len(path) == 0 which it does because path starts as "" recursively
                for letter in mapping[digits[len(path)]]:
                    myfunc(path + letter)


        myfunc("")
        return res



#2/6/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        def solve(path):
            if len(digits) == len(path):
                res.append(path)
            else:
                for i in mapping[digits[len(path)]]:
                    solve(path + i)

        solve("")
        return res


#2/8/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ""
        res = []
        mapping = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        def findletter(path):
            if len(digits) == len(path):
                res.append(path)
            else:
                for neighbor in mapping[digits[len(path)]]:
                    findletter(path + neighbor)
                    
        findletter("")
        return res


#2/9/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        mapping = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        def dfs(path):
            if len(digits) == len(path):
                res.append(path)
            else:
                for mover in mapping[digits[len(path)]]:
                    dfs(path + mover)
        dfs("")
        return res


#2/11/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ""
        res = []
        mapping = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        def f(path):
            if len(digits) == len(path):
                res.append(path)
                return
            else:
                for i in mapping[digits[len(path)]]:
                    f(path + i)
                    #("", a)
                    #(a, d)
                    #(a, e)
                    #(a, f)
                    #("", b) 
                    #(b, d) - i passes b to path as path was previously "" but is now b! i says to path - son, hold for me as i traverse

 
        f("")
        return res
        

#2/13/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        res = []
        mapping = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        def f(child):
            if len(digits) == len(child):
                res.append(child)
                return
            else:
                for parent in mapping[digits[len(child)]]:
                    f(child + parent)
        res = []
        f("")
        return res

#2/15/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        mapping = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        def f(assistant):
            if len(digits) == len(assistant):
                res.append(assistant)
                return
            else:
                for i in mapping[digits[len(assistant)]]:
                    f(assistant + i)
        res = []
        f("")
        return res

#2/19/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        #could we make right hand side string instead of list? YES!
        mapping = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        def starter(child):
            if len(child) == len(digits):
                res.append(child)
                return
            else: #not hit max length yet
                for i in mapping[digits[len(child)]]:
                    starter(child + i)
        res = []
        starter("")
        return res

#2/23/24:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        def f(path):
            if len(path) == len(digits):
                res.append(path)
                return
            else:
                for i in mapping[digits[len(path)]]:
                    f(path + i)

        res = []
        f("")
        return res
