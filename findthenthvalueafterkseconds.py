#medium
#54.6% acceptance rate
#3179

#You are given two integers n and k.

#Initially, you start with an array a of n integers where a[i] = 1 for all 0 <= i <= n - 1. After each second, you simultaneously update each element to be the sum of all its preceding elements plus the element itself. For example, after one second, a[0] remains the same, a[1] becomes a[0] + a[1], a[2] becomes a[0] + a[1] + a[2], and so on.

#Return the value of a[n - 1] after k seconds.

#Since the answer may be very large, return it modulo 109 + 7.



#my own solution using python3 after a small adjustement:

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = (10 ** 9) + 7
        initial = [1] * n
        print(initial)
        res = []
        while k > 0:
            for i in range(1, len(initial)):
                initial[i] += initial[i - 1]
            initial[0] = 1
            k -= 1
        return initial[-1] % mod #need to read the instructions that we need to divide by mod!


#my own easy solution using python3 on 3/13/25:

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        #[1, 1, 1, 1]
        mod = ((10 ** 9) + 7)
        start = [1] * n
        for i in range(k):
            start = list(itertools.accumulate(start))
        return start[n - 1] % mod
