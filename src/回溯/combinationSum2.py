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
        #repeat =[]
        def backtrack(candidates, target, sum, startindex):
            if sum == target:
                res.append(path[:])
            for i in range(startindex, len(candidates)):
                if sum + candidates[i] > target: return
                #i>startindex代表着什么意思？i>startindex,代表着同一数层。i=startindex代表同一树枝。
                if i > startindex and candidates[i] == candidates[i - 1]: continue
                #[[1, 1, 3], [1, 2, 2], [2, 3], [5]]
                #这两种去重方式有什么不同？
                #用repeat就仅代表着同一树枝不能有重复元素。
                # if candidates[i] in repeat:
                #     continue
                #[[2, 3], [2, 3], [5]]

                #repeat.append(candidates[i])
                #if candidates[i] in repeat:continue
                sum += candidates[i]
                path.append(candidates[i])

                backtrack(candidates, target, sum, i + 1)
                sum -= candidates[i]
                #repeat.pop()
                path.pop()

        candidates = sorted(candidates)
        backtrack(candidates, target, 0, 0)
        return res

A =Solution()
candidates=[1,2,3,1,5,2]
target = 5
print(A.combinationSum2(candidates,target))