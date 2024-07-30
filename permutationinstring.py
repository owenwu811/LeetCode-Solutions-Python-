



#my wrong solution passing 93/108 test cases:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        needfroms2 = Counter(s1)
        tmp = needfroms2
        matched = 0
        for we, char in enumerate(s2):
            if char not in needfroms2:
                needfroms2 = tmp
            if char in needfroms2:
                needfroms2[char] -= 1
                if needfroms2[char] == 0:
                    matched += 1
            if matched == len(needfroms2):
                return True
        return False


#python3 solution:

#one of my failing test cases from above was this:
#s1 = "hello"
#s2 = "ooolleoooleh"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
  
        left = 0 #0
        right = len(s1) #5
        key = "".join(sorted(s1))	#"ehllo"

        while right <= len(s2) + 1: #5 <= 12
            string = s2[left:right] #oooll 
            if "".join(sorted(string)) == key: #oooll != ehllo, so increment left and right to slide the window one position right in s2 (bigger string)!
                return True 
            left += 1 #1 #this is sliding the window to the right because we haven't found a valid rearrangement yet!
            right += 1 #6 #this is sliding the window to the right because we haven't found a valid rearrangement yet!

        return False
