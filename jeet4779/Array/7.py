'''
Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. 
There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.'''
'''
Explaination: Seems like a DP problem but since we don't have to maintain the order, we can sort this given array. Now start is 0 and end is M-1, this will create a 
window of M size means it will contain M chocolates that are going to be distributed to these M studnets, since we have to only know the difference bewteen the maximum
and minimum of the window, we will know that by arr[end]-arr[start] and ovbiously we will kind of slide this M size window on the array and we will do this until we cannot
form any valid window.
'''
class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        start = 0
        end = M-1
        ans = 9999999
        while end< N:
            ans = min(A[end]-A[start],ans)
            start+=1
            end+=1
        return ans
