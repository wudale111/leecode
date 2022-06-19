'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
'''
class Solution:
    def __init__(self):
        self.path =[]
        self.res =[]

    def patition(self,s):
        self.backtrack(s,0)
        return self.res

    def backtrack(self,s,startindex):
        if startindex==len(s):
            return self.res.append(self.path[:])
        for i in range(startindex,len(s)):
            #如何截取字符串
            p = s[startindex:i+1]
            if self.ishuiwen(p):
                self.path.append(p)
            else:
                continue
            self.backtrack(s,i+1)
            self.path.pop()

    def ishuiwen(self,s):
        i,j =0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i +=1
            j -=1
        return True
A =Solution()
s = 'aabb'
print(A.patition(s))
    