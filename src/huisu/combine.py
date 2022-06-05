'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

'''
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(n, k, startindex):
            # if len(path) > k:
            #     return
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(startindex, n + 1):
                path.append(i)
                dfs(n, k, i + 1)
                path.pop()

        dfs(n, k, 1)
        return res
A = Solution()
A.combine(5,2)
print(A.combine(5,2))