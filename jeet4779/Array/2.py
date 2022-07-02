'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''
'''
Explanination: Used simple counting sort algorithm to do that.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = [0]*(3)
        for i in nums:
            c[i]+=1
        k=0
        for i in range(3):
            
            while(c[i]>0):
                nums[k] = i
                k+=1
                c[i]-=1
