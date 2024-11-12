
#1023
#medium

#Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

#A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. You may insert each character at any position and you may not insert any characters.

 

#Example 1:

#Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
#Output: [true,false,true,true,false]
#Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
#"FootBall" can be generated like this "F" + "oot" + "B" + "all".
#"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
#Example 2:

#Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
#Output: [true,false,true,false,false]
#Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
#"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".


#my own solution using python3:

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for q in queries:
            flag = True
            qupperidx, patternupperidx = [], []
            for i, letter in enumerate(q):
                if letter.isupper():
                    qupperidx.append(i)
                    if letter not in pattern or pattern.count(letter) < q.count(letter):
                        flag = False
            for i, p in enumerate(pattern):
                if p.isupper():
                    patternupperidx.append(i)
                    if p not in q or q.count(p) < pattern.count(p):
                        flag = False
                if p.islower():
                    if p not in q or q.count(p) < pattern.count(p):
                        flag = False
            #print(qupperidx, patternupperidx)
            if len(qupperidx) >= 2 and len(patternupperidx) >= 2:
                biggerstr = q[qupperidx[0]: qupperidx[1] + 1]
                print(biggerstr)
                smallerstr = pattern[patternupperidx[0]: patternupperidx[1] + 1]
                print(smallerstr)
                for i in range(len(smallerstr)):
                    if i < len(smallerstr) and i < len(biggerstr):
                        if smallerstr[i].islower() and biggerstr[i].islower():
                            if smallerstr[i] != biggerstr[i]:
                                if biggerstr.count(smallerstr[i]) < smallerstr.count(smallerstr[i]):
                                    flag = False


            res.append(flag)
        return res


                
                
        #"CompetitiveProgramming"
        #between C and P dosen't have two os!
        #"CooP"

        #"ControlPanel"
        #"CooP"
