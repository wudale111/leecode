"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(candidates, target, sum, startindex):
            if sum > target:
                return
            if sum == target:
                res.append(path[:])
                return

            for i in range(startindex, len(candidates)):
                path.append(candidates[i])
                sum += candidates[i]
                # if sum + candidates[i] >target: return  #如果 sum + candidates[i] > target 就终止遍历
                backtrack(candidates, target, sum, i)
                sum -= candidates[i]
                path.pop()

        backtrack(candidates, target, 0, 0)
        return res