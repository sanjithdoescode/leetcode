'''
Day - 10
Word Subsets

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
'''

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxf=[0]*26
        tem=[0]*26
        for word in words2:
            for w in word:
                tem[ord(w)-ord('a')]+=1
            for i in range(26):
                maxf[i]=max(maxf[i],tem[i])
            tem=[0]*26
        res=[]
        for word in words1:
            for w in word:
                tem[ord(w)-ord('a')]+=1
            flag=True
            for i in range(26):
                if maxf[i]>tem[i]:
                    flag=False
                    break
            if flag:
                res.append(word)
            tem=[0]*26
        return res
