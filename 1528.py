'''
Day - 2
Problem - 1528
Shuffle String

You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
'''
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = ""
        for ctrl_var in range (len(s)):
            shuffled += s[indices.index(ctrl_var)]
        return shuffled
