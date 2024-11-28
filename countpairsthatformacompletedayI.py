
#3184
#easy

#Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

#A complete day is defined as a time duration that is an exact multiple of 24 hours.

#For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

 

#Example 1:

#Input: hours = [12,12,30,24,24]

#Output: 2

#Explanation:

#The pairs of indices that form a complete day are (0, 1) and (3, 4).



#my own solution using python3:

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cur = []
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    cur.append([i, j])
        print(cur)
        return len(cur)
                    
