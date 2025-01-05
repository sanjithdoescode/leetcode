'''
Day - 5
Problem - 848
Shifting Letters

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.
'''

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for i in range(n-2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i+1]) % 26
            
        ans = []
        for i, c in enumerate(s):
            idx = (ord(c) - ord('a') + shifts[i]) % 26
            ans.append(chr(idx + ord('a')))
        return "".join(ans)
