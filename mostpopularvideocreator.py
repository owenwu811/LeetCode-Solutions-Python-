

#2456
#medium

#You are given two string arrays creators and ids, and an integer array views, all of length n. The ith video on a platform was created by creators[i], has an id of ids[i], and has views[i] views.

#The popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator with the highest popularity and the id of their most viewed video.

#If multiple creators have the highest popularity, find all of them.
#If multiple videos have the highest view count for a creator, find the lexicographically smallest id.
#Note: It is possible for different videos to have the same id, meaning that ids do not uniquely identify a video. For example, two videos with the same ID are considered as distinct videos with their own viewcount.

#Return a 2D array of strings answer where answer[i] = [creatorsi, idi] means that creatorsi has the highest popularity and idi is the id of their most popular video. The answer can be returned in any order.

 

#Example 1:

#Input: creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]

#Output: [["alice","one"],["bob","two"]]


#my own solution using python3:

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = defaultdict(list)
        for i, c in enumerate(creators):
            d[c].append([ids[i], views[i]])
        print(d)
        pop = dict()
        videos = defaultdict(list)
        for k in d:
            cur = 0
            mostviewed = 0
            for a in d[k]:
                cur += a[1]
                mostviewed = max(mostviewed, a[1])
            print(mostviewed)
            pop[k] = cur
            for a in d[k]:
                if a[1] == mostviewed:
                    videos[mostviewed].append(a[0])
        print(pop)
        person = max(pop.values())
        print(videos) #go through videos
        newpop = dict()
        for a in pop:
            if pop[a] == person:
                newpop[a] = pop[a]
        #print(newpop)
        eliminate = dict()
        for n in newpop:
            if n in d:
                eliminate[n] = d[n]
        #print(eliminate)
        neweliminate = defaultdict(list)
        for e in eliminate:
            highestc = 0
            for video in eliminate[e]:
                highestc = max(highestc, video[1])
            for video in eliminate[e]:
                if video[1] == highestc:
                    neweliminate[e].append(video)
        print(neweliminate)
        sample = ["three", "one"]
        for n in neweliminate:
            neweliminate[n].sort(key=lambda x: x[0])
        print(neweliminate)
        res = []
        for n in neweliminate:
            tmp = []
            if neweliminate[n]:
                tmp.append(n)
                tmp.append(neweliminate[n][0][0])
            res.append(tmp)
        print(res)
        return res
