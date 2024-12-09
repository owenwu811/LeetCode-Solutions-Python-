

#1604
#medium

#LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

#You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

#Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

#Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

#Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

 

#Example 1:

#Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
#Output: ["daniel"]
#Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").


#my own solution using python3:

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        res = []
        for i, k in enumerate(keyName):
            keyTime[i] = keyTime[i].replace(":", "")
            d[k].append(int(keyTime[i]))
            cur = 0
            d[k].sort()
            now = []
            for i in range(1, len(d[k])):
                if d[k][i] - d[k][i - 1] <= 100:
                    if d[k][i] not in now:
                        now.append(d[k][i])
                    if d[k][i - 1] not in now:
                        now.append(d[k][i - 1])
                    cur += 1
            now.sort()  
            print(now, k)
            flag = False
            for i in range(len(now) - 2):
                substr = now[i: i + 3]
                print(substr)
                if substr[-1] - substr[0] <= 100:
                    flag = True
            if cur >= 2 and flag:
                print(k)
                if k not in res:
                    res.append(k)
        print(d)
        res.sort()
        return res
