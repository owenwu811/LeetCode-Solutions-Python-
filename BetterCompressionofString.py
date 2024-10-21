

#3167
#medium

#You are given a string compressed representing a compressed version of a string. The format is a character followed by its frequency. For example, "a3b1a1c2" is a compressed version of the string "aaabacc".

#We seek a better compression with the following conditions:

#Each character should appear only once in the compressed version.
#The characters should be in alphabetical order.
#Return the better compression of compressed.

#Note: In the better version of compression, the order of letters may change, which is acceptable.

 

#Example 1:

#Input: compressed = "a3c9b2c1"

#Output: "a3b2c10"

#Explanation:

#Characters "a" and "b" appear only once in the input, but "c" appears twice, once with a size of 9 and once with a size of 1.

#Hence, in the resulting string, it should have a size of 10.

#my own solution using python3:

class Solution:
    def betterCompression(self, compressed: str) -> str:
        print(compressed)
        cur = []
        characters = []
        for c in compressed:
            if not (c.isdigit()):
                characters.append(c)
            cur.append(c)
        print(cur)
        i = 0
        d = dict()
        numbers = []
        while i < len(compressed):
            tmp = ""
            while i < len(compressed) and cur[i].isdigit():
                tmp += cur[i]
                i += 1
            i += 1
            print(tmp)
            if tmp:
                numbers.append(str(tmp))
        print(numbers)
        print(characters)
        d = dict()
        for i, char in enumerate(characters):
            if char not in d:
                d[char] = 0
            d[char] += int(numbers[i])
        print(d)
        sortedd = dict(sorted(d.items(), key=lambda x: x[0]))
        print(sortedd)
        ans = ""
        for k in sortedd:
            ans += k
            ans += str(sortedd[k])
        return ans
