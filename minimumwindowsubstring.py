

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
