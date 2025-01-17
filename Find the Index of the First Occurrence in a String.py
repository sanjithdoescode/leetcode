'''
Day -16
Problem - 28
Find the Index of the First Occurrence of a String

Given two strings
needle and haystack,
return the index of the first occurence of needle in haystack, or -1 if needle is not part of haystack.

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1 
