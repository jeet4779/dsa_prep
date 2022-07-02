'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''
'''
Explaination: Idea is to bring the non-zero element to the front. Simple two pointer approach j will look for zero's and i will be pointing two the current position where we will store next non-zero element.
when we find a non-zero element, we have to swap it with current ith position else the current element will be zero and we will keep incrementing j.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while(i< len(nums) and j<len(nums)):
            if nums[j]==0:
                j+=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
