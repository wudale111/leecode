'''
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
示例:
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:
给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
'''

class Solution:
    def increasesub(self,nums):
        path = []
        res = []


        def backtrack(nums,startindex):
            #这里能用path[:]?path此时是什么，应该是个数组？
            if len(path[:]) >= 2:
                res.append(path[:])
            for i in range(startindex,len(nums)):
                #因为第一个数nums[i-1]会超出范围，所以要用nums[i]>nums[-1]来限定递增条件。
                repeat = []
                if nums[i] in repeat:
                    #为什么是continue不是berak?
                    continue
                #为什么会要这个判断？不是第一次循环就是大于等于1的？
                if len(path)>=1:
                    #新循环进来的数，要比前面添加过的数path数组最后一个数大、而不是比nums数组最后一个数大！！！！
                    #if nums[i] < nums[-1]:
                    if nums[i]<path[-1]:
                        continue
                #repeat会不会有重叠问题？
                repeat.append(nums[i])
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        backtrack(nums,0)
        return res
A =Solution()
nums=[4,7,6,7]
print(A.increasesub(nums))

