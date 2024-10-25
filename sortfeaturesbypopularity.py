
#1722
#medium

#You are given a string array features where features[i] is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features they like. You are given a string array responses, where each responses[i] is a string containing space-separated words.

#The popularity of a feature is the number of responses[i] that contain the feature. You want to sort the features in non-increasing order by their popularity. If two features have the same popularity, order them by their original index in features. Notice that one response could contain the same feature multiple times; this feature is only counted once in its popularity.

#Return the features in sorted order.

 

#Example 1:

#Input: features = ["cooler","lock","touch"], responses = ["i like cooler cooler","lock touch cool","locker like touch"]
#Output: ["touch","cooler","lock"]
#Explanation: appearances("cooler") = 1, appearances("lock") = 1, appearances("touch") = 2. Since "cooler" and "lock" both had 1 appearance, "cooler" comes first because "cooler" came first in the features array.
#Example 2:

#Input: features = ["a","aa","b","c"], responses = ["a","a aa","a a a a a","b a"]
#Output: ["a","aa","b","c"]


#my own solution using python3:

class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        tmp = []
        for r in responses:
            cur = []
            h = r.split(" ")
            #print(h)
            for word in h:
                cur.append(word)
            tmp.append(cur)
        print(tmp)
        d = defaultdict(int)
        for f in features:
            for t in tmp:
                if f in t:
                    d[f] += 1
        print(d)
        leftover = []
        for f in features:
            if f not in d:
                leftover.append(f)

        d = dict(sorted(d.items(), key=lambda x: x[1]))
        print(d)
        newd = dict()
        for k in d:
            if d[k] not in newd:
                newd[d[k]] = []
            newd[d[k]].append(k)
        newd = dict(sorted(newd.items(), key=lambda x: x[0], reverse=True))
        print(newd)
        final = []
        for key in newd:
            current = []
            for a in newd[key]:
                current.append([a, features.index(a)])
            current = sorted(current, key=lambda x: x[1])
            final.append(current)
        print(final)
        ans = []
        for f in final:
            #print(f)
            for j in range(len(f)):
                print(f[j])
                ans.append(f[j][0])
        if leftover:
            ans.extend(leftover)
        return ans
