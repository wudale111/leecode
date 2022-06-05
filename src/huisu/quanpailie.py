'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
'''

# class Solution:
#     def __init__(self):
#         self.path =[]
#         self.res =[]
#         self.repeat = []
#
#     def quanpai(self,nums):
#         self.backtrack(nums,self.repeat)
#         return self.res
#
#     def backtrack(self,nums,repeat):
#         if len(self.path) == len(nums):
#             return self.res.append(self.path[:])
#
#         for i in range(0,len(nums)):
#             if nums[i] in self.repeat:
#                 continue
#             self.repeat.append(nums[i])
#             #if i > startindex and nums[i] == nums[i - 1]:continue
#             self.path.append(nums[i])
#             self.backtrack(nums,repeat)
#             #self.backtrack(nums,0)
#             self.path.pop()
#             self.repeat.pop()

from typing import List
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.repeat = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        #self.backtrack(nums, self.repeat)
        self.backtrack(nums)
        return self.res

    #def backtrack(self, nums, repeat):
    def backtrack(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return

        for i in range(0, len(nums)):
            if nums[i] in self.repeat:
                continue
            self.repeat.append(nums[i])
            self.path.append(nums[i])
            #self.backtrack(nums, repeat)
            self.backtrack(nums)
            self.path.pop()
            self.repeat.pop()
A =Solution()
nums =[1,2,3]
print(A.permute(nums))

# from typing import List
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []  #存放符合条件结果的集合
#         path = []  #用来存放符合条件的结果
#         used = []  #用来存放已经用过的数字
#         #def backtrack(nums,used):
#         def backtrack(nums):
#             if len(path) == len(nums):
#                 return res.append(path[:])  #此时说明找到了一组
#             for i in range(0,len(nums)):
#                 if nums[i] in used:
#                     continue  #used里已经收录的元素，直接跳过
#                 path.append(nums[i])
#                 used.append(nums[i])
#                 #backtrack(nums,used)
#                 backtrack(nums)
#                 used.pop()
#                 path.pop()
#         #backtrack(nums,used)
#         backtrack(nums)
#         return res
#         #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
#         #[ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
# A =Solution()
# nums =[1,2,3]
# print(A.permute(nums))