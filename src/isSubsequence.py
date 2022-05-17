'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
'''
'''
aab
abc
true
aab会导致index不变，所以不能用这个max方法来判断自增。
'''
# s = input()
# t = input()
# index = -1
# time = 0
# for i in range(len(s)):
#     if s[i] in t:
#         index = max(index,t.index(s[i]))
#         if index==t.index(s[i]):
#             time +=1
#         else:
#             print('false')
#
#     else:
#         print('false')
# if time == len(s):
#     print('true')


#双指针
#这里为什么不能用for呢？因为不是遍历字符串s或者t,
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=j=0
        n,m=len(s),len(t)
        while(i<n and j<m):
            if s[i] ==t[j]:
                i +=1
            j +=1
        #判断是否为子序列，最终要靠i指针能否走完s字符串。
        return i==n
        # n, m = len(s), len(t)
        # i = j = 0
        # while i < n and j < m:
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == n
A = Solution()
s= 'abce'
t = 'abdadsdac'
print(A.isSubsequence(s,t))


