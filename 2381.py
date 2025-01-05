'''
Day - 5
Problem - 2281
Shifting Letters II

You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.
'''

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n, sz= len(s), len(shifts)
        app=[0]*(n+1)
        for b, e, d in shifts:
            app[b]+=(d*2-1)
            app[e+1]-=(d*2-1)
        app=list(accumulate(app))
        s0=[]
        for i, c in enumerate(s):
            t=(app[i]+ord(c)-97)%26+97
            if t<97: t+=26
            s0.append(chr(t))
        return "".join(s0)
