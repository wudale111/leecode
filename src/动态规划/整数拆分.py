'''
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。

示例 1:

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3,n+1):
            for j in range(1,i):
                #为什么要dp[i]??因为在递推公式推导的过程中，每次计算dp[i]，取最大的而已。??因为这里有个遍历j到i,比较哪个dp[i]大
                dp[i]=max(dp[i],j*(i-j),dp[i-j]*j) #dp[3]=max(dp[3],6,1)
        return dp[-1]

A = Solution()

print(A.integerBreak(10))