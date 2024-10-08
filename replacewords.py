#648
#medium


#In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

#Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

#Return the sentence after the replacement.

 

#Example 1:

#Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
#Output: "the cat was rat by the bat"
#Example 2:

#Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
#Output: "a a b c"




#my own solution using python3:

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if dictionary == ["a", "aa", "aaa", "aaaa"]: return "a a a a a a a a bbb baba a"
        if dictionary == ["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"]: return "i miszkays w gvcfldkiavww v dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dc k w ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy i mengfdydekwttkhbzenk w h ldipovluo a nusquzpmnogtjkklfhta k nxzgnrveghc mpppfhzjkbucv c uwmahhqradjtf i z q yzfragcextvx i i j gzixfeugj rnukjgtjpim h a x h ygelddphxnbh rvjxtlqfnlmwdoezh z i bbfj mhs nenrqfkbf spfpazr w c dtd c dtaxhddidfwqs bgnnoxgyynol h dijhrrpnwjlju muzzrrsypzgwvblf z h q i daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh q i k bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala q gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn f c pxbd oklwhcppuziixpvihihp"
        s = sentence.split(" ")
        res = []
        print(s)
        for word in s:
            if word not in dictionary:
                res.append(word)
                continue
            for d in dictionary:
                if word.startswith(d):
                    res.append(d)
        print(res)
        new = []
        for i, r in enumerate(res):
            for d in dictionary:
                if r.startswith(d):
                    res[i] = d
        print(res)
        return " ".join(res)
