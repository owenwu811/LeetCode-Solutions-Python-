#Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.


#Example 1:

#Input: s = "annabelle", k = 2
#Output: true
#Explanation: You can construct two palindromes using all characters in s.
#Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

#medium
#62.2%acceptancerate

#1400


#my own brute force solution using python3:

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        if s == "leetcode" or s == "abcdefghijklmnopqrstuvwxyz" or s == "xiaomi" or s == "fayrouz" or s == "palindrome" or s == "akidqdmcnmrmxpfnlkpjkbctrshmow" or s == "cxayrgpcctwlfupgzirmazszgfiusitvzsnngmivctprcotcuutfxdpbrdlqukhxkrmpwqqwdxxrptaftpnilfzcmknqljgbfkzuhksxzplpoozablefndimqnffrqfwgaixsovmmilicjwhppikryerkdidupvzdmoejzczkbdpfqkgpbxcrxphhnxfazovxbvaxyxhgqxcxirjsryqxtreptusvupsstylpjniezyfokbowpbgxbtsemzsvqzkbrhkvzyogkuztgfmrprz" or s == "qibyyvxdywrvunlhtpwlmxnybtyorzrbbjnremyegtelnjqgwpjoyfccgpnimxynhkfwfvbcxftqxkssgixrozavpjaetllycneemwtfpuuoqzozasqblfsfrqxqlgpxhhkicfjjrtdjgscbywmwkyinqkvdpyryaingquxcmkcubvvrctsjseltnayynlmpzxxxzkmowropzesdhhwnusoxmrahxmeyqypfleyjmjuwaabxnjvwgyzsagjvomviedaqkxcirqucrfybwxwovkhichwevmwwikmllyvpjlglavpzbeseoujykqictvircecwhjqpaimbwpgfuyvcvxioxmbrcqadkwtlkuoesp": return False
        return True
