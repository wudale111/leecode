'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

'''
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        #空字符串来相加存字符组合，数组的组合用数组，字符串组合要s=''做字符串相加
        s =""
        letterMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        #如果没有下面这条，输入""，输出[""]。答案是：[]
        if not len(digits): return res
        def backtrack(digits,startindex,s):
            #那么终止条件就是如果index 等于 输入的数字个数（digits.size）了
            if startindex == len(digits):
                return res.append(s)

            digit =int(digits[startindex])
            letter = letterMap[digit]
            for i in range(len(letter)):
                s += letter[i]
                backtrack(digits,startindex+1,s)
                #截取字符串开头到末尾（不汉堡最后一个字符）
                s= s[:-1]
        backtrack(digits,0,s)
        return res



