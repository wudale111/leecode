'''
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。 
#不可以包含重复的组合打赏曹张新村
'''
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(candidates, target, sum, startindex):
            if sum == target:
                res.append(path[:])
            for i in range(startindex, len(candidates)):
                if sum + candidates[i] > target: return
                if i > startindex and candidates[i] == candidates[i - 1]: continue
                sum += candidates[i]
                path.append(candidates[i])

                backtrack(candidates, target, sum, i + 1)
                sum -= candidates[i]
                path.pop()

        candidates = sorted(candidates)
        backtrack(candidates, target, 0, 0)
        return res