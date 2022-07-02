'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

'''
Explaination: Simple binary search question, only one extra problem is if the array contains duplicate element then the binary search may retrun the same index twice like
[3,3] which is not acceptable.Hence we wil handle this separately, if two elements are equal than linealry search from index of first+1 to know the index of another
element with same value but different index( since question says there always would be an valid solution).
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i =0
        j= len(nums)-1
        new =sorted(nums)
        while(i<j):
            if(new[i]+new[j]==target):
                break
            elif(new[i]+new[j]>target):
                j-=1
            elif(new[i]+new[j]<target):
                i+=1
        if(new[i]==new[j]):
            temp = nums.index(new[i])
            ans=0
            for j in range(temp+1,len(nums)):
                
                if(nums[j]==new[i]):
                    ans=j
                    break
            return nums.index(new[i]),ans
        else:
            return nums.index(new[i]),nums.index(new[j])
