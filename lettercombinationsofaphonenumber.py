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
