#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
'''
class Solution:
    def jumpFloor(self , number: int) -> int:
        #因为dp[i-1]过i=1，dp[0]在数组中没值，所以递归公式求不出，所以number=1另外定义。
        if number == 1:
            return 1
        #db[]的长度为n+1，因为列表头多了一个零阶,无论如何索引从0开始，要加number个数，所以大小number+1
        dp = [0] * (number+1 )
        dp[1] = 1
        dp[2] = 2
        for i in range(3, number+1 ):
            dp[i] = dp[i - 1] + dp[i - 2]
            #dp[3] = dp[2]+dp[1]
            #dp[4] = dp[3]+dp[2]
            #dp[5] = dp[4]+dp[3]
        return dp[-1]

# class Solution:
#     def jumpFloor(self , number: int) -> int:
#         a = b = 1
#         for i in range(2, number + 1):
#             a, b = b, a + b
#         return b

A = Solution()
print(A.jumpFloor(3))