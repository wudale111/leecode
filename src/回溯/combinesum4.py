'''
M个数的列表，可能有重复，需要去重，然后给定一个N，
求数组中N个最小值和N个最大值值值的和，
如果 N个最小和N个最大值的值中有重叠，则返回-1
'''


class Solution:
    def combinesum(self,nums,k):
        path=[]
        res=[]
        def backtrack(nums,k,startindex):
            if len(path)==k:
                return res.append(path[:])
            for i in range(startindex,len(nums)):
                #if i > 0 and nums[i] == nums[i - 1]:
                #[[1, 2], [1, 3], [2, 3]]
                #[[1, 1], [1, 2], [1, 3], [2, 3]]
                if i>startindex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums,k,i+1)
                path.pop()
        backtrack(nums,k,0)
        return res

a=Solution()
nums=[1,2,3,1]
k=2
#nums=list(set(nums))
nums.sort()
b=a.combinesum(nums,k)
print(b)
# print(len(b))
# c=[]
# for j in b:
#     c.append(sum(j))
# print(c)
# c.sort()
# print(c[0]+c[-1])