from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n=len(envelopes)
        envelopes.sort()
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
                    print(dp[i])
        num=max(dp)
        return num
a=Solution()

print(a.maxEnvelopes([[1,2],[1,3],[5,6],[3,4]]))

# Dynamic programming.
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums: return 0
#         dp = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     print(dp[i],i)
#         return max(dp)
# a=Solution()
#
# print(a.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))