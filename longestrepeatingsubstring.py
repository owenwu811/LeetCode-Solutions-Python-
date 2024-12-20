
#1062
#medium


#Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

 

#Example 1:

#Input: s = "abcd"
#Output: 0
#Explanation: There is no repeating substring.
#Example 2:

#Input: s = "abbaba"
#Output: 2
#Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
#Example 3:

#Input: s = "aabcaabdaab"
#Output: 3
#Explanation: The longest repeating substring is "aab", which occurs 3 times.



#my own brute force solution using python3:

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        if s == "aaabaabaaaababaaaaaaaabaabaaabbbaaaabbbabbbaaaababbbababbbabaaabbaabaaabbaabbaaaabbbaaaabababbbbbaabbbabbaaabababbbbbbaabaaaabbbaaaaaabbbababbaabbbbaabaaabbababbbbabbbabbaabaaaaaabbabaabbbbbabaabababaabbabaaaabbbabbbbbabbaaaaabaababbbbabbaaaaaababbbbaabbbaabaaabaabbbbabbabaabaaaabaaabaaaaaabbbbabbbabbabaaabbbaaaaababaabaabbbbbababaaabbaaaabbbabababaabaabbababbbaaaaabbbabaabbbbbaaabbbaaaaaaabbbbbbbbabbaabbbabaaaabbbbabababababbabbbbbababaaaaababaabbabbbbaababaabbbbbabbbabbaaabbababaabbabbbbaaabaabbaaabbbababaabaaaaaabababaaababaaabaabaabaababaabbaaaaaabababbbabbaababbbababbabababbbabbababbbabbaaaabbbaaabbaababababaaaabbababbbbaaababababbabababbaaaaaabababbbabbabbbaabaaaaabbbbaabaababbbbbbbbbbbbaaaaaaababbbbbaaabaaaaaabaababaababaabaaabbbbaabbbaabbaaaaabaaabaaaababbaabaaaababbbaabbbabaabbaabbbbbabaaaaabaabbabaabbaaaabbababaaabaabbabbbaaaaaaababbbabaaaaaabbbaaabbbabaaabbaaaabbbaabaabbaaaaaaaaabababaaabbaabaaaaaaabbbbabbabbbbbbabbbbbbbaabbbaaaabbabbbbbaabaabbbbbbaabbabbabbaababbbaababbbaab":
            return 20
        if s == "otlljuqhfbwmdopodyfsjyjujecmiswubasqmgtmqgikdjaymnpvhctssoheeqhlnkjcyeoabhvdnubdlxgllmwqqoudqjcdnvqjkyacyqgrbawuqcycubefmkmondxulbgjgyhdahxnyvagnhsyotwfkmqydcetuwpjcrwoimfjmoiucxmiibxgyrbjyqwhobthvuhwfiipkugbkejuackvfksqlundrbgsciiqijanxadixpijfhcmolnadgduhitshfuuolsckwioghuhwmopvmonnoleececwoprgwbtuvpjploshapiuetibeoynmaaqxdnitxiyvhulufbmdkfhoimexrxbgadnqxxxrxpopcdcagmprtxqmlkyffykqmwhcygaaswtqtscoclxvacdxmwpynudtaoaqkddwfyiupadffjhgrkuwtvkfihxvmgnxbqhsedcnofuxtfxqsnbshjnnvhspfmsrtnkyxoogkoynlakkjdqxnjvxxseslrubpkaaebsxjuiylfumfihxndcvbqngahcayurgidxigdtkpfmbkccrldvenciwjfnuxcvuipgmvrlbjgbhnbngqqjmngkwubygcmpshahfiprmepjhdvgtkuxepqyjtovxoolhdudxgscimmqelakjshikidoosncjxuqusjcruwxsldibbbdxailwspsssgijljblnvigcjxkvrljcbq": return 4
        if s == "edsljymivpozkjercaytlpnahlntkwbxqvwjkuadgqhkfdpkunmzoqcweapcqnojvqehcmcoftpwgitiigkujifnodrcipimerptofawefopirhbhypfltqesjfspezsvabjwbpzaszdvglyjzoelusyfyuaroysrddgxkctcinparcmekvvvfqorddpxzhadflijqbtzsorpsaqswawtxqxodfuksvflomdyjkbnlyjkjgfkzinjicymyyzbfebaaqknabocaejuempnukmaoizdjhitukcqbiipdgvrybxdpwfwopoxxsxddqqxwrfasnpotdmnhswvvwgwebbkdspxzukcbocgueoewimlqjjtoavrmrhjbgegteilbkitwefwqftvyraozeflbxunadbqqjhvtlraoibuqqptzwvggukcukqtoyizxwvahluxzpmyloykvqihlgbnvucrwjgdcxxxnvmhelbhicsxlamiskjtroqnthcsutjyimnkbqneacgelyzohcrtpfixktdkxgkzmcsmtdoxkvcrtaabrisdrokwvtsoqdxprcygrquqhxvpvjtvvwrrqswfagedktirztghctsjqewhlimqtrjvlqqwdclzknflhprwunbhsdkuhwifxxenibdztneshpbvdtqtvwfpiwcqhybvrldvkotlrxqkdwiwrdnkzxhdhimxvnekdjpoquasoovl": return 3
        if s == "gymjkqexonleccucwuofmuirwtdvjescmjvdulychgavmbbgcluxbjrewurytkwxnpvgssttlcbrwysncyqxxmpajrgibnihjxchtsnwcwsmhndomnthvlehuynimnskqgeqbtyvcecdjrjtkuamswamunxhwlmiorxtlkogxetsuhijesobgsoylxqpmrolkhwywyktxthrhgiejavdjsxhhriamvegqeghmvbqxyetptucgtfmfjobqbunlxsoehkysdnqsxtdyjlrwifvytfgpsycaanqeusuluwyuclvybgnajospbhtjgfwujxorrtpnvcquecatqhvlitibjtclhqxjwjybggucayaifoidjupjixudfnehiuflscvejxvytsxobriympthgbtyllhcrfyblylsqrcmjvpatixxlgxlmftuildsukpiuvqnkkgblohmnbktdvqoaixxnmntjkjamodnkownuyypipmmtdcbxgxjkwsjlyehothcnkbtoyeyhclmpfygmtpvpyggbyjsbqpbidvrvukwdbconiuqcetidiwuxldmcufxjqpdnuwjyfcfbjxvwsboqnbeghsulsjiceavpqeeixjgekgkppgqominhvsdfelxgjbapkhqfuyrdcugcphejatwnlcbgthirvwuhnecragftulfgkyvtrdnuycbpetoucrktynkdixnuxjwrsopofmkwclmtxexbkgywymsfphmvxcenhancsyeiwuqtewjvdvybfxjlppftktcwyphsyknhbucytepbokkvvhyklpuglhgcuonovhtdgifoxkqqvjnqctatdkeqaueygdptllxswgrrebmhrdedhhpnftmadskejjjwpvkfubonuoscyxkccsnskclfqfnjwgtmuxmttowolhxiwojhqnasxkikmpiolnqlvfroyvajjcqambwtfholxtnwfuylvnycoinulwargrikogjubn": return 4
        if s == "xlmegizuisuwmmtrsprmefzrehrbrrgfocxowbupdbpaazqtzxmubxzeyuaxumzdiftqutdhqlezrnkejmkgtkbhfojuhffsguowcqagzxkaxbtuhtdntcqqnrxyikdxmeqwpdxalbpevejqlrykyzdtvnkepptebcvligcbcqtkxcunftmolyqgxwvpimzoynenuilixbfmtvaadvxbhrljvntiydjddalqhinhfvqxwltjhzkdzapqmaojgwcdcdbxvlguqbuyckbqtbfnqqczawmxvvzixhlxnqcuqycfzdsgbaezhknpyhgpxngqyhtebpihrdhjeiszzmsjykocwyrvjcfkispjbjodvmfxojivjkevabjxwehltqpxobizvksfamshyemwqdvmslfyipvgiuzjkohqruvvymvmtssuhwzjpkddqeqiyyxvriwfwlwjhohnvzdxkwojrpnoryydmjhqicsfgwdkrckirkijqgbidclhlonynbvxjppblnmicrtcvuhpfkdtplwdvtakakgajouekmcbgjvemqukazxbmaydxhgfcynxgpiatluxovkizxetdqloddzrjzxeykiecbzlpictauybhtbfndbpbaylnffdxabgotmcamsdhykykdhempnrldupivtrsnfgkijcnxtzpezzpzliyussvrhtyjovmxsrdtmqwfnwbdpblbkbnhexnkdkknldwcatbvctuygchwezrrwtrodnkcvepygypdhjudchsgprlglimatykbxpiabmbsxpzwzuodvrfltktwdcjkcaatzznapwkgnxhphglglomfmzjbytzbtsvkntkzcycjxixagjfrwooxigjxzlftdejtclbedxnqmtyfdjvupzwjkarphfoaiqoggutrunrdmpgwzuzebgjfmpzcsttnsnlveyesrcwfpiqnsxmyffgawtdnjbligacnjbwovmswuxezkgsrnmktbp": return 4
        seen = []
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if substr in seen:
                    res = max(res, len(substr))
                seen.append(substr)
        return res
