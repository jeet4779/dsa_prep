//https://leetcode.com/problems/find-the-duplicate-number/
//arsh sheet

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        nums.sort()
        while(i<j):
            if nums[i]==nums[i+1]:
                return nums[i]
            else:
                i+=1
         
