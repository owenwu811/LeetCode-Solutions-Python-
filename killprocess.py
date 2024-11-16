#582
#medium

#You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

#Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

#When a process is killed, all of its children processes will also be killed.

#Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.


#my own solution using python3:

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = defaultdict(list)
        sd = dict() 
        for i, p in enumerate(ppid):
            d[p].append(pid[i])
        print(d)
        #print(sd)
        queue = deque() 
        queue.append(kill)
        res = []
        while queue:
            a = queue.popleft() 
            print(a)
            res.append(a)
            for nei in d[a]:
                queue.append(nei)
        return res
