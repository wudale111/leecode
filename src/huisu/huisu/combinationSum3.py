'''
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
'''
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(k,sum,n,startindex):
            if len(path)>k:
                return
            if len(path)==k and sum ==n:
                res.append(path[:])
                return

            for i in range(1,9):

                path.append(i)
                sum += i
                dfs(k,sum,n,i+1)
                sum -=i
                path.pop()

        dfs(k,0,n,1)
        return res

A = Solution()
n=4
k=2
A.combinationSum3(2,4)
print(A.combinationSum3(2,4))

