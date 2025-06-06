
#1817
#medium


#You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

#Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

#The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

#You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

#Return the array answer as described above.

 

#Example 1:

#Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
#Output: [0,2,0,0,0]
#Explanation:
#The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
#The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
#Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.


#my own soution using python3:


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        #[id, time]
        #unique times?
        d = defaultdict(list)
        for l in logs:
            d[l[0]].append(l[1])
        print(d)
        #[number of users UAM = 1, 2, 3, 4, 5] - k
        #0: [5, 2, 5] - user 0 has UAM of 2
        #1: [2, 3] - user 1 has UAM of 2
        newd = defaultdict(list)
        for key in d:
            newd[len(set(d[key]))].append(key)
        print(newd)
        res = []
        for i in range(1, k + 1):
            print(i)
            if i not in newd:
                res.append(0)
            else:
                res.append(len(newd[i]))
        print(res)
        return res
        
