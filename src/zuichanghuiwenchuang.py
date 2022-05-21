'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。
'''
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []  #放已经回文的子串
        # 双指针法判断是否是回文串
        def isPalindrome(s):
            n = len(s)
            i, j = 0, n - 1
            while i < j:
                if s[i] != s[j]:return False
                i += 1
                j -= 1
            return True

        def backtrack(s, startIndex):
            if startIndex >= len(s): # 如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
                res.append(path[:])
                return
            for i in range(startIndex, len(s)):
                p = s[startIndex:i+1] # 获取[startIndex,i+1]在s中的子串
                if isPalindrome(p): # 是回文子串
                    path.append(p)
                else: continue #不是回文，跳过
                backtrack(s, i + 1)
                path.pop() #回溯过程，弹出本次已经填在path的子串
        backtrack(s, 0)
        return res