

#609
#medium

#Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

#A group of duplicate files consists of at least two files that have the same content.

#A single directory info string in the input list has the following format:

#"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
#It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

#The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

#"directory_path/file_name.txt"
 

#Example 1:

#Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
#Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

#my own solution using python3:

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #a 1.txt(abcd) 2.txt(efgh)
        #c 3.txt(abcd)
        #c/d 4.txt(efgh)
        #so since 2.txt(efgh) and 4.txt(efgh) have the same () content, they go in the same group
        d = defaultdict(list)
        for p in paths:
            #print(p)
            a = p.split(" ")
            print(a)
            for g in a:
                if "(" in g and ")" in g:
                    first = g.index("(")
                    last = g.index(")")
                    key = g[first + 1:last]
                    without = g[:first] 
                    beg = a[0] + "/"
                    print(first, last, key, without, beg)
                    d[key].append(beg + without)
        print(d)
        #[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        #{'abcd': ['root/a/1.txt', 'root/c/3.txt'], 'efgh': ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']})
        res = []
        flag = 0
        for k in d:
            if len(d[k]) == 1:
                flag += 1
        if flag == len(d):
            return []
        for k in d:
            if len(d[k]) == 1:
                continue
            tmp = []
            for a in d[k]:
                tmp.append(a)
            res.append(tmp)
        return res
