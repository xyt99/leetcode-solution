'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
    # python3
    # def twoSum(self, nums: List[int], target: int) -> List[int]:

'''
key:
range() return an iterable object,not list in python 2
range(stop)
range(start, stop[, step])
contains start but not contains stop,start's default number is 0.
eg: 
for i in range(1,100,10):
    print(i)
# 1 11 21 31 41 51 61 71 81 91
'''
