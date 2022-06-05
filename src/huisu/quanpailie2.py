'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

'''

class Sulution:
    def __init__(self):
        self.path=[]
        self.res=[]
        self.repeat=[]

    def quanpai(self,nums):
        self.backtrack(nums)
        return self.res

    def backtrack(self,nums):
        if len(self.path)==len(nums):
            return self.res.append(self.path[:])

        for i in range(0,len(nums)):
            if nums[i] in self.repeat:
                continue


# from typing import  List
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         # res用来存放结果
#         if not nums: return []
#         res = []
#         used = [0] * len(nums)
#         def backtracking(nums, used, path):
#             # 终止条件
#             if len(path) == len(nums):
#                 res.append(path.copy())
#                 return
#             for i in range(len(nums)):
#                 if not used[i]:
#                 used[i - 1] == true，说明同一树支nums[i - 1]
#                 使用过
#                 used[i - 1] == false，说明同一树层nums[i - 1]
#                 使用过
#                 如果同一树层nums[i - 1]
#                 使用过则直接跳过
#                     if i>0 and nums[i] == nums[i-1] and not used[i-1]:
#                         continue
#                     used[i] = 1
#                     path.append(nums[i])
#                     backtracking(nums, used, path)
#                     path.pop()
#                     used[i] = 0
#         # 记得给nums排序
#         backtracking(sorted(nums),used,[])
#         return res

