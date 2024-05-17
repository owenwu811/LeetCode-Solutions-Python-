

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        tdict, matched, l, start, windowlenS = Counter(t), 0, 0, 0, len(s) + 1
        for r, sch in enumerate(s):
            if sch in tdict:
                tdict[sch] -= 1
                if tdict[sch] == 0:
                    matched += 1
            while matched == len(tdict):
                if windowlenS > r - l + 1:
                    start = l
                    windowlenS = r - l + 1
                removedchar = s[l]
                l += 1
                if removedchar in tdict:
                    if tdict[removedchar] == 0:
                        matched -= 1
                    tdict[removedchar] += 1
        if windowlenS < len(s):
            return s[start:start + windowlenS]
        elif windowlenS == len(s):
            return s
        else:
            return ""



#explanation: ORIGINALLY, our tdict represents what we need from s to satisfy t: 'a': 1, 'b': 1, 'c': 1. as we find t's characters from s, we now say we need ONE LESS FROM S. if we shrink the window, we take the character - a - we kicked out of the left side of the window and saw we now still need one MORE OF THAT CHARACTER FROM S by incrementing the dictionary value - a: 0 becomes a: 1 - to say we still need one more A from s to satisfy t. 
#explanation 2: ONLY WHAT IS IN OUR WINDOW CURRENTLY can count towards our allowance from s to satisfy t. We only shrink the window once by kicking the character out from the leftmost side of our window, and if the character - a - we kicked out counted towards the allowance towards satisfying t, we must take this allowance away once since we only shrink by a character ONCE and increment the count in the dictinoary to say we still need one more a - 'a': 0 becomes 'a': 1 to say we still need one more a to satisfy t



#my solution - python3:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        startsaver = 0
        endsaver = len(s) + 1
        ws = 0
        matched = 0
        tdict = Counter(t)
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                #only matched when we satisfy all occurences of a character 
                if tdict[schar] == 0:
                    matched += 1
            while matched == len(tdict):
                if endsaver > we - ws + 1:
                    startsaver = ws
                    endsaver = we - ws + 1
                kickout = s[ws]
                ws += 1
                if kickout in tdict:
                    #only if we completely satisfied the character in t do we rollback our progress on matched  
                    if tdict[kickout] == 0:
                        matched -= 1
                    #we need one more
                    tdict[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver:startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""

#important: matched variable tracks the frequency of characters from s that have fully satisified t. so means how many letters in the dictionary have values of 0 - a:0, b: 0, c: 1 - matched would be 2 because 2 letters - a and b - from s have FULLY SATISFIED t




#another practice run - my own solution in python3:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #note that, even if we comment out the 1st line, the algorithm still works 
        if len(s) < len(t): return ""
        startsaver = 0
        endsaver = len(s) + 1
        tdict = Counter(t)
        fullysatisfied = 0
        ws = 0
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                if tdict[schar] == 0:
                    fullysatisfied += 1
            while fullysatisfied == len(tdict):
                #since we've now found a solution, we're after the goal of finding the minimum window that satisfies t from s
                #we - ws + 1 is the new smaller but valid window
                if endsaver > we - ws + 1:
                    startsaver = ws
                    endsaver = we - ws + 1
                #whether we found a smaller window or not, we need to shrink the window
                kickoutchar = s[ws]
                ws += 1
                if kickoutchar in tdict:
                    if tdict[kickoutchar] == 0:
                        fullysatisfied -= 1
                    #as long as the left char we are kicking out is in tdict as a key, we need to reflect the fact that we need one more of that character now since we shrunk the window - this is independant of if we fully satisfied that character from s in t or not
                    tdict[kickoutchar] += 1
        #we finished looping through s, and endsaver represents the end of the smallest window that satisfies t
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""



#super important: if you put "tdict[kickoutchar] += 1" before "if tdict[kickoutchar] == 0:" rather than after, then fullysatisfied -= 1 would never execute: to illustrate here, let's say it was supposed to be 'a': 0, which would decrement fully satisfied, but now that you've incremented it before, you would get 'a': 1, which wouldn't decrement fully satisfied now, messing up the result, causing the "while fullysatisfied == len(tdict)" to be true instead of false because you shrunk the window, so now s isn't fully satisfying t since the a from the beginning of s = ADOBECODEBANC is now gone from the window DOBEC, but this was never reflected in fully satisfied, leading to complete wrong results
                      

#2/1/24 practice:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tdict = Counter(t)
        startsaver = 0
        ws = 0
        matched = 0
        endsaver = len(s) + 1
        for we, schar in enumerate(s):
            #if schar exists in tdict as a key
            if schar in tdict:
                tdict[schar] -= 1
                #only when we fully satisfied that character from s in t do we increment matched by 1 because we want matched to equal the length of tdict aka the number of unique keys in tdict counting by the left column
                if tdict[schar] == 0:
                    matched += 1
            while matched == len(tdict):
                if endsaver > we - ws + 1:
                    #we found a new smallest window, so save those indicies and begin shrinking
                    startsaver = ws
                    endsaver = we - ws + 1
                kickout = s[ws]
                ws += 1
                #there's a possibility that the character we are kicking out from the left of the window is not a character in tdict
                if kickout in tdict:
                    #fully satisfied - if we made this <= 0, it would be incorrect because if a: 0, c: 0, b: -1, we have one more than enough Bs to satisfy t, so that dosen't mean we still need one more, so we don't need to decrement matched from 3 to 2 if we kicking out b once, which already has one more than we need to satisfy t - we just need to increment b from b: -1 to b: 0 AND NOT TOUCH MATCHED
                    if tdict[kickout] == 0:
                        matched -= 1
                    #we need one more allowance of that character
                    tdict[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""


#2/2/24 practice:

if len(s) < len(t): return ""
        tdict = Counter(t)
        startsaver = 0
        endsaver = len(s) + 1
        ws = 0
        matched = 0
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                if tdict[schar] == 0:
                    matched += 1
            while matched == len(tdict): #while t is satisfied
                if endsaver > we - ws + 1: #we found a smaller window
                    endsaver = we - ws + 1
                    startsaver = ws
                #we always need to shrink
                kickout = s[ws] 
                ws += 1
                if kickout in tdict:
                    if tdict[kickout] == 0:
                        matched -= 1
                    tdict[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""


#2/3/24 practice:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #there's no way to make up all characters (including duplicates) in t if s is shorter than t in length
        if len(s) < len(t): return ""
        tdict = Counter(t)
        startsaver = 0
        endsaver = len(s) + 1
        matched = 0
        ws = 0
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                if tdict[schar] == 0:
                    matched += 1
            while matched == len(tdict):
                if endsaver > we - ws + 1:
                    startsaver, endsaver = ws, we - ws + 1
                #we need to shrink
                kickout = s[ws]
                ws += 1
                #if we are kicking a character from our s window that we used to satisfy tdict
                if kickout in tdict:
                    if tdict[kickout] == 0: 
                    #you can't combine these two ifs because that would indent tdict[kickout] += 1 forward, and just because you found a smaller window dosen't mean you still owe one more - only if matched was 0 and you got rid of one of them would you owe one more, so saying we need one more is reserved for if the one we kickout out was in our tdict
                        matched -= 1
                    tdict[kickout] += 1
        if len(s) > endsaver:
            #because these are indicies, but endsaver was translated into a length, we want to up to but not including since we are indexing into s with startsaver + endsaver
            return s[startsaver: startsaver + endsaver]
        if len(s) == endsaver:
            return s
        else:
            return ""
                

#2/4/24 refresher:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s has length of m and t has length of n
        #we want the smallest substring inside of s that includes atleast everything in t without having to be contiguous 
        if len(s) < len(t): return ""
        startsaver = 0
        #because endsaver is intended to hold a value that will be larger than the length of our string, we can use len(s) + 1 or even infinity becauase we will be shrinking later anways to a value that is garunteed to be smaller at the worst case - (len(s)) itself
        endsaver = float('inf')
        tdict = Counter(t)
        matched = 0
        ws = 0
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                if tdict[schar] == 0:
                    matched += 1
            while matched == len(tdict):
                if endsaver > we - ws + 1:
                    startsaver = ws
                    endsaver = we - ws + 1
                kickout = s[ws]
                ws += 1
                if kickout in tdict:
                    if tdict[kickout] == 0:
                        matched -= 1
                    tdict[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""
            

#2/5/24 refresher:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        startsaver = 0
        endsaver = len(s) + 1
        tdict = Counter(t)
        ws = 0
        matched = 0
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                #after this executes, regardless of true or false, ALWAYS check the while condition to see if we've satisfied all characters
                if tdict[schar] == 0:
                    matched += 1
            #after if conditions evaluate, always check if we've satisfied all characters
            while matched == len(tdict):
                if endsaver > we - ws + 1:
                    startsaver = ws
                    endsaver = we - ws + 1
                #shrinking window
                kickout = s[ws]
                ws += 1
                if kickout in tdict:
                    #if it was previously exactly satsified meaning we don't have an abundance of characters, and we're kicking it out, now we need just one more to satisfy
                    if tdict[kickout] == 0:
                        matched -= 1
                    #regardless of it was exactly satisfied or not, we now need one more of that character that we kicked out 
                    tdict[kickout] += 1
        if len(s) > endsaver:
            #ENDSAVER IS WE - WS + 1, SO IF WE = 12 AND WS = 9, ENDSAVER WOULD BE (12 - 9 + 1) = 4, SO IF STARTSAVER IS 9, WE WOULD GET S[9:4], WHICH IS WRONG, SO ENDSAVER ISN'T A GOOD VARIABLE NAME FOR THIS
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""


#better variable names:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        startsaver = 0
        windowsizelength = len(s) + 1
        tdict = Counter(t)
        ws = 0
        matched = 0
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                #after this executes, regardless of true or false, ALWAYS check the while condition to see if we've satisfied all characters
                if tdict[schar] == 0:
                    matched += 1
            #after if conditions evaluate, always check if we've satisfied all characters
            while matched == len(tdict):
                if windowsizelength > we - ws + 1:
                    startsaver = ws
                    windowsizelength = we - ws + 1
                #shrinking window
                kickout = s[ws]
                ws += 1
                if kickout in tdict:
                    #if it was previously exactly satsified meaning we don't have an abundance of characters, and we're kicking it out, now we need just one more to satisfy
                    if tdict[kickout] == 0:
                        matched -= 1
                    #regardless of it was exactly satisfied or not, we now need one more of that character that we kicked out 
                    tdict[kickout] += 1
        #think windowsize length is HOW LONG startsaver lays out the floor mat to make the actual windowsize of the carpet!
        if len(s) > windowsizelength:
            #ENDSAVER IS WE - WS + 1, SO IF WE = 12 AND WS = 9, ENDSAVER WOULD BE 4, SO IF STARTSAVER IS 9, WE WOULD GET S[9:4], WHICH IS WRONG, SO ENDSAVER ISN'T A GOOD VARIABLE NAME FOR THIS
            return s[startsaver: startsaver + windowsizelength]
        elif len(s) == windowsizelength:
            return s
        else:
            return ""

#most clear variable names - my solution in python3 (best one that is most clear):


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        windowsizeinlength = float('inf')
        matched, ws, carpetroller = 0, 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
            while matched == len(need):
                if windowsizeinlength > we - ws + 1:
                    carpetroller = ws
                    windowsizeinlength = we - ws + 1
                kickout = s[ws]
                ws += 1
                if kickout in need:
                    if need[kickout] == 0:
                        matched -= 1
                    #always need because the one we are kicking out of our s window was in what we needed (tdict)
                    need[kickout] += 1
        if len(s) > windowsizeinlength:
            return s[carpetroller: carpetroller + windowsizeinlength]
        elif len(s) == windowsizeinlength:
            return s
        else:
            return ""


#2/8/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        carpetroller = 0
        difference = len(s) + 1
        matched = 0
        ws = 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
            #keys are unique, so we only have a as the key ONCE in our need dictionary
            while matched == len(need):
                if difference > we - ws + 1:
                    difference = we - ws + 1
                    carpetroller = ws
                kickout = s[ws]
                ws += 1
                if kickout in need:
                    if need[kickout] == 0:
                        matched -= 1
                    need[kickout] += 1
        if len(s) < difference:
            return ""
        elif len(s) == difference:
            return s
        else:
            return s[carpetroller: carpetroller + difference]


#2/11/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s can't satisfy t if s is less than t
        if len(s) < len(t): return ""
        carpetroller, matched, ws = 0, 0, 0
        difference = float('inf')
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
            while matched == len(need):
                #we found a working window, so now find the smallest one
                #using len(s) instead of difference here would fail test case s = "a" t = "a" as we would return "" instead of "a"
                if difference > we - ws + 1:
                    difference = we - ws + 1
                    carpetroller = ws
                #shrink window one character at a time from left side of list
                kickout = s[ws]
                ws += 1
                if kickout in need:
                    if need[kickout] == 0:
                        matched -= 1
                    need[kickout] += 1
        if len(s) > difference:
            return s[carpetroller: carpetroller + difference]
        elif len(s) == difference:
            return s
        else:
            return ""


#2/12/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        startsaver, endsaver = 0, float('inf')
        matched, ws = 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
            while matched == len(need):
                if endsaver > we - ws + 1:
                    endsaver = we - ws + 1
                    startsaver = ws
                kickout = s[ws]
                ws += 1
                if kickout in need:
                    if need[kickout] == 0:
                        matched -= 1
                    need[kickout] += 1
        if len(s) > endsaver: return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver: return s
        else: return ""
 
#again:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if s is smaller than t, there's no chance of s fully satisfying t
        if len(s) < len(t): return ""
        need = Counter(t)
        carpetroller, difference, matched, ws = 0, float('inf'), 0, 0
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                #the only time any requirement was satisfied was the line above, so this would be the 1st time any character would be quantified as matched
                if need[schar] == 0:
                    matched += 1
            while matched == len(need): #fully satisfied t
                if difference > we - ws + 1: #now, looking to satisfy smallest window requirement
                    carpetroller = ws
                    difference = we - ws + 1
                kickout = s[ws]
                ws += 1
                if kickout in need:
                    if need[kickout] == 0:
                        matched -= 1
                    #we always need one more since we are kicking that one character out by shrinking our window
                    need[kickout] += 1 #will return control flow to "while matched == len(need)", and if that while is False, then will flow control back to "for we, schar in enumerate(s)"
        #finished looping through s
        if len(s) > difference:
            return s[carpetroller: carpetroller + difference]
        elif len(s) == difference:
            return s
        else:
            return ""

#2/13/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        matched = 0
        difference = float('inf')
        carpetroller = 0
        ws = 0
        need = Counter(t)
        for we, schar in enumerate(s):
            #the dictionary dosen't START with any values of any keys as 0
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1 #we use matched to keep track of it we satisfied entire t or not
            while matched == len(need):
                #we have to record this satisfactory window before trying to shrink
                if difference > we - ws + 1:
                    carpetroller, difference = ws, we - ws + 1
                kickout = s[ws]
                ws += 1 #actually shrinking window
                if kickout in need: #this time, since we actually modified the dictionary values by decrementing them in "need[schar] -= 1", it has the possiblity to be a 0
                    if need[kickout] == 0: #if we satisfied that letter without any extras
                        matched -= 1 
                    need[kickout] += 1
        if len(s) > difference: return s[carpetroller: carpetroller + difference]
        elif len(s) == difference: return s
        else: return ""
                    
#2/14/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        matched = 0
        difference = float('inf')
        carpetroller = 0
        ws = 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
            while matched == len(need):
                if difference > we - ws + 1:
                    difference = we - ws + 1
                    carpetroller = ws
                kickout = s[ws]
                ws += 1
                if kickout in need:
                    if need[kickout] == 0:
                        matched -= 1
                    need[kickout] += 1
        if len(s) > difference:
            return s[carpetroller: carpetroller + difference]
        elif len(s) == difference: return s
        else: return ""

#2/15/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #not possible to satisfy t and all of t's potential duplicates with s if s is shorter than t
        if len(s) < len(t): return ""
        matched, carpetroller, ws, difference = 0, 0, 0, float('inf')
        need = Counter(t)
        #we will slide our window through s and jot down the dimensions of that window if it's valid
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0: #fully satisfied ONE MORE letter, so mark this in matched as satisfiying one more letter than before
                    matched += 1 #based on the mechanism of matched, matches represents each UNIQUE CHARACTER IN T BEING FULLY SATISFIED BY OUR WINDOW IN S
            while matched == len(need): #we fully satisfied s in t, so we also need to find the smallest window in s that satisfies t
                windowlength = we - ws + 1
                if difference > windowlength:
                    difference = windowlength
                    carpetroller = ws
                kickout = s[ws] #shrink the window now since we jotted down that window dimension if it was the smallest so far
                ws += 1
                if kickout in need:
                    if need[kickout] == 0: #we had exactly satisfied that character in s from t that we just kickout out, so we have to reflect this in match to say we disatisfied one more letter than before
                        matched -= 1 #matched just cares about the frequency of characters because matched represents each character being fully satisfied
                    need[kickout] += 1 #we are reflecting needing one more of this character in our need dictionary
        #we only can determine the minimum window substring after we have slid our window through our entire s string
        if len(s) > difference: return s[carpetroller: carpetroller + difference]
        elif len(s) == difference: return s
        else: return ""

#2/17/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        matched, carpetroller, ws, difference = 0, 0, 0, float('inf')
        need = Counter(t)
        for we, schar in enumerate(s): #we slide the window through s with our ws and we
            if schar in need: #exists as a key in our dictionary 
                need[schar] -= 1 #say we need one less of that character - no duplicates as keys in dictionary
                if need[schar] == 0: #fully satisfied one character - no duplicates as keys in dictionary even though letters may be repeated in t - that is what the value of the key value pair in our dictionary is for
                    matched += 1
            while matched == len(need): #fully satisfied window, so find minimum
                if difference > we - ws + 1: 
                    difference = we - ws + 1 #saving that window as a potential minimum
                    carpetroller = ws
                kickout = s[ws]
                ws += 1 #actually shrinking window
                if kickout in need: #if the character we kicked out exists as a key in our need dictionary, make the appropriate changes
                    if need[kickout] == 0: #change matched because matched depends on the value to the key in the dictionary before we kickout out the window
                        matched -= 1
                    need[kickout] += 1
        if len(s) > difference: return s[carpetroller: carpetroller + difference]
        elif len(s) == difference: return s
        else: return "" #without this line, we would fail s = "a" t = "b" because we would return null instead of ""

#2/20/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if s is shorter than t, then s can't satisfy all of t including all of t's duplicates, so we can return an empty string since there would be no substring
        if len(s) < len(s): return ""
        ws, matched, carpetroller = 0, 0, 0
        difference = float('inf')
        need = Counter(t)
        #we slide the window through s
        for we, schar in enumerate(s):
            if schar in need:
                #we satisfied that character once 
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1 #we matched with one character in s by fully satisfying it including all of it's duplicates - a key in the need dictionary
                #whether this entire while block is indented to the first if or 2nd if is irrelevant - still works!!
                while matched == len(need):
                    if difference > we - ws + 1:
                        difference = we - ws + 1
                        carpetroller = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > difference:
            return s[carpetroller: carpetroller + difference]
        elif len(s) == difference: return s
        else: return ""

#2/28/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        cr, d, ws, matched = 0, float('inf'), 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
            while matched == len(need):
                if d > we - ws + 1:
                    d = we - ws + 1
                    cr = ws
                kickout = s[ws]
                ws += 1
                if kickout in need:
                    if need[kickout] == 0:
                        matched -= 1
                    need[kickout] += 1
        if len(s) > d:
            return s[cr: cr + d]
        elif len(s) == d:
            return s
        else:
            return ""

#3/2/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s has to fully satisfy t - if not, then return an empty substring
        if len(s) < len(t): return ""
        carpetroller, matched, ws, difference = 0, 0, 0, float('inf')
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1 #even if characters appear multiple times in t, this is progress because need dict only contains unique keys
                while matched == len(need): #every single character was matched
                    if difference > we - ws + 1:
                        difference = we - ws + 1 #mark current state as a window inside of s
                        carpetroller = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0: #we will use need[kickout] later, so do the check to see if we backtracked progress now
                            matched -= 1
                        need[kickout] += 1
        #once we have finished iterating through s, we can anwser the final question of it we can satisfy t with s
        if len(s) > difference: #difference is the size of our smallest window
            return s[carpetroller: carpetroller + difference]
        elif len(s) == difference:
            return s
        else:
            return ""


#3/4/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #every character in t is included in our s window
        if len(s) < len(t): return ""
        matched, ws, carpetroller, difference = 0, 0, 0, float('inf')
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need):
                    if difference > we - ws + 1:
                        difference = we - ws + 1
                        carpetroller = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > difference:
            return s[carpetroller: carpetroller + difference]
        elif len(s) == difference:
            return s
        else: return ""


#3/8/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): ""
        start, length, need, matched, ws = 0, float('inf'), Counter(t), 0, 0
        for we, schar in enumerate(s): #we slide the window through s
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need):
                    if length > we - ws + 1:
                        length = we - ws + 1
                        start = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > length: #found smaller valid window
            return s[start: start + length]
        elif len(s) == length:
            return s
        else: return ""

#3/14/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        matched, start, difference, ws = 0, 0, float('inf'), 0
        need = Counter(t)
        for we, schar in enumerate(s): #we slide the window throughout s
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need): #fully satisfied t with our window in s, so look for smallest window requirement
                    if difference > we - ws + 1: #always true on 1st turn
                        difference = we - ws + 1 #update to save smallest window result at this point
                        start = ws
                    #shrink window
                    kickout = s[ws] #get the value at the index to reflect changes in our need dict and matched
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1 #we need one more
        if len(s) > difference: #we have a smaller valid window that fully satisfies t, so return it
            return s[start: start + difference]
        elif len(s) == difference:
            return s
        else: return ""


#3/19/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return "" #every character in t is included in the window means can s satisfy t, not the other way around
        start, difference, ws, matched = 0, float('inf'), 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1 #need starts as each value being more than 0 because wouldn't appear if was 0 cause letter dosen't exist  in s
                if need[schar] == 0:
                    matched += 1
                while matched == len(need): #we satisfied every character
                    if difference > we - ws + 1:
                        difference = we - ws + 1
                        start = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need: #kickout is part of s, which may not be in t, so we are shrinking the window to look for the smallest satisfactory window
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > difference:
            return s[start: start + difference]
        if len(s) == difference: return s
        else: return ""

#3/24/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return "" #already not possible if s is shorter than t
        start, diff, matched, ws = 0, float('inf'), 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need: #need starts out as above 0
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need):
                    if diff > we - ws + 1:
                        diff = we - ws + 1
                        start = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > diff:
            return s[start: start + diff]
        if len(s) == diff: return s
        else: return ""

#3/29/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        ws, diff, matched, start = 0, float('inf'), 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need): #satisfied s 
                    if diff > we - ws + 1:
                        diff = we - ws + 1
                        start = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > diff:
            return s[start: start + diff]
        elif len(s) == diff: return s
        else: return ""
 
#4/8/24 (missed):

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we want the minimum of s that satisifes t, not the other way around
        if len(s) < len(t): return ""
        ws, start, end, matched = 0, 0, float('inf'), 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0: 
                    matched += 1
                while matched == len(need): #every character in s is included in t
                    if end > we - ws + 1:
                        end = we - ws + 1
                        start = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > end:
            return s[start: start + end]
        elif len(s) == end: return s
        else: return ""


#practice again:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we want the smallest portion of s that fully satisfies t
        if len(s) < len(t): return "" #s can't satisfy t if it's already smaller than t - whole s is smaller than whole t
        start, end, matched, ws = 0, float('inf'), 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1 #fully satisfied that char in t
                while matched == len(need): #satisfied all characters in t
                    if end > we - ws + 1: #find smaller window
                        end = we - ws + 1
                        start = ws
                    kickout = s[ws] 
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > end:
            return s[start: start + end]
        elif len(s) == end: return s
        else: return ""

#4/8/24 practice again:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        start, end, matched, ws = 0, float('inf'), 0, 0
        need = Counter(t) #represents total from t that we need from s
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1 #fully satisfied t with our current window indicated by ws and we
                while matched == len(need): #matched caught as many characters in s meaning satisfied as many different characters in s as keys in need, which are all the different characters in t
                    if end > we - ws + 1:
                        end = we - ws + 1
                        start = ws
                    kickout = s[ws] #we are on task of finding smallest part of s that fully satisfies t
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > end:
            return s[start: start + end]
        elif len(s) == end: return s
        else: return ""

#4/9/24 refresher:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        start, end, ws, matched, need = 0, float('inf'), 0, 0, Counter(t)
        for we, schar in enumerate(s): #we want to satisfy t with smallest part of s
            if schar in need:
                need[schar] -= 1 #need one less from s
                if need[schar] == 0:
                    matched += 1 #one more char in t satisfied
                while matched == len(need): #total distinct chars satisfied == number of keys in tdict aka number of distinct chars in t
                    if end > we - ws + 1:
                        end = we - ws + 1
                        start = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0: #if it was turning point of being perfectly matched
                            matched -= 1
                        need[kickout] += 1
        if len(s) > end:
            return s[start: start + end]
        if len(s) == end: return s
        else: return ""


#4/17/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #smallest s that encompasses t
        if len(s) < len(t): return ""
        res, start, end, ws, matched = 0, 0, float('inf'), 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need): # we completed every character in t (each t character is a key of the dictionary, which must be unique)
                    if end > we - ws + 1:
                        end = we - ws + 1
                        start = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1 #matched only changes if we complete a letter in t fully. it dosen't track progress of a letter
                        need[kickout] += 1
        if len(s) > end: #we are comparing len of s input with the length of the smallest recorded window, which is end, not we!
            return s[start: start + end]
        elif len(s) == end:
            return s
        else: return ""
                        
                    

#4/23/24:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #smallest part of s that fits everything inside of t including any duplicates in t
        if len(s) < len(t): return ""
        startsaver, endsaver, ws, matched = 0, float('inf'), 0, 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need):
                    if endsaver > we - ws + 1:
                        endsaver = we - ws + 1 #exactly the length of the window
                        startsaver = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else: return ""

#5/7/24 refresher:

class Solution(object):
    def minWindow(self, s, t):
        #find small part of s that fits t
        if len(s) < len(t): return ""
        startsaver, endsaver, ws, matched = 0, float('inf'), 0, 0
        need = Counter(t)
        for we, char in enumerate(s):
            if char in need:
                need[char] -= 1
                if need[char] == 0:
                    matched += 1
                while matched == len(need):
                    if endsaver > we - ws + 1:
                        endsaver = we - ws + 1
                        startsaver = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else: return ""

#5/17/24 refresher:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we want the minimum portion of s that fully satisifes t
        if len(s) < len(t): return "" #we know that s cannot satisfy t
        windowstart, windowend, matched = 0, float('inf'), 0
        ws = 0
        need = Counter(t)
        for we, schar in enumerate(s):
            if schar in need:
                need[schar] -= 1
                if need[schar] == 0:
                    matched += 1
                while matched == len(need): #we satisfied all characters in t
                    if windowend > we - ws + 1:
                        windowend = we - ws + 1
                        windowstart = ws
                    kickout = s[ws]
                    ws += 1
                    if kickout in need:
                        if need[kickout] == 0:
                            matched -= 1
                        need[kickout] += 1
        if len(s) > windowend:
            return s[windowstart: windowstart + windowend]
        elif len(s) == windowend:
            return s
        else:
            return ""

        
