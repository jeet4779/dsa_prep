'''
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

'''
There are many eays of doing this and since question doesn't mention that we cannot use an inbuilt method, then why not, just don't index hehe.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
