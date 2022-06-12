from typing import List
class Solution:
    def subsets(self,nums:List[int])->List[List[int]]:
        res = []
        path = []
        #startindex起到什么作用，？怎么定义初始值？
        def backtrack(nums,startindex):
            res.append(path[:])
            if startindex >= len(nums):
                return
            for i in range(startindex,len(nums)):
                path.append(nums[i])
                print(path)
                backtrack(nums,i+1)
                path.pop()

        backtrack(nums,0)#为什么这里startindex初始化为0，因为是遍历数组的索引从0开始。
        return res
A = Solution()
nums = [1,3,4,6]

print(A.subsets(nums))

       #  nums = [1,3,4,6]
       # 1\  i=0,path [1]
       #     2\  startindex=1, path [1,3]
       #         3\  startindex=2, path [1,3,4]
       #            4\ startindex=3 , path [1,3,4,6] ->[1,3,4]
       #               5\ startindex=4, return




