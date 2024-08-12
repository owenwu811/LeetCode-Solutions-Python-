



#python3 solution using backtracking:

#we use backtracking and constraint checking where once we've placed a dot, we only have three possible positions for the next dot - after one digit, after two digits, or after three digits. This constraint helps reduce the number of combinations we need to consider. Instead of validating 990 combinations, we only have to check 3 x 3 x 3 = 27 combinations. 

#we implement the backtrack function that takes the position of the previously placed dot, prev_dot, and the number of dots, dots, to place them as arguments:

#1. iterate over the three available slots, curr_dot, to place a dot
#2. check if the current segment from the previous dot to the current one is valid
#if yes, place the dot and add the current segment to our segments list
#check if all 3 dots are placed
#if yes, concatenate the segments list into a string and add the ip string to the result list
#if not, proceed to place the next dots backtrack(curr_dot, dots - 1)
#remove the last dot to backtrack 

#in summary: place each dot after a gap of one digit. start from the last segment and check if it's a valid segment. if it's true, then add this segment to the segments list and backtrack to place the dot to complete previous segments. recursively call the backtrack function to make all possible valid ip addresses. the time complexity is 0(1) since we only have to check 3 x 3 x 3 = 27 combinations
#the space complexity is also constant since we have 19 valid ip addresses at most


from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment: str) -> bool:
            if len(segment) > 3 or len(segment) == 0: #each segment's length should be less than 3
                return False
            #check if the current segment is valid for either one of the following conditions:
            #1. check if the current segment is less or equal to 255
            #2. check if the length of the segment is 1. the first character of segment can only be '0' if the length of the segment is 1
            if segment[0] == '0' and len(segment) > 1:
                return False
            return 0 <= int(segment) <= 255
        
        def backtrack(start: int, path: List[str]):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if valid(segment):
                    path.append(segment)
                    backtrack(end, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result
