
#811
#medium

#A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

#A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

#For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
#Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

 

#Example 1:

#Input: cpdomains = ["9001 discuss.leetcode.com"]
#Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
#Explanation: We only have one website domain: "discuss.leetcode.com".
#As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.


#my own solution using python3:

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(list)
        for c in cpdomains:
            now = c.split(" ")
            print(now)
            after = now[-1].split(".")
            print(after)
            h = deque()
            for i, a in enumerate(after[::-1]):
                h.appendleft(a)
                #print(h)
                #print(".".join(h))
                a = c.split(" ")
                #print(a[0])
                d[".".join(h)].append(a[0])
        print(d)
        ans = []
        for k in d:
            totsum = 0
            for a in d[k]:
                totsum += int(a)
            #print(cursum)
            cookie = str(totsum) + " " + k
            print(cookie)
            ans.append(cookie)
        return ans
