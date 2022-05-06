from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex,n+1):
                path.append(i)  #处理节点
                # print(path)
                # print(i,"11111111111")

                backtrack(n,k,i+1)  #递归
                #print(i,"22222222222")
                path.pop()  #回溯，撤销处理的节点
                #print(i,"333333333333")

        backtrack(n,k,1)
        #5,2,1 startindex=1,i=1
# 5 2 2 ->[1,2]  startindex =2,i=2,path弹出2，i+1=3，继续调用递归函数，此时递归函数判断path=k,结束递归。i一直加到5，在path中弹出5，结束第二次递归。继续第一次递归
#这是清算第一次递归，弹出1，继续for循环.
               #5 2 4
        #      5 2 3 return 循环结束，返回第二次DFS，第二次DFS继续完后代码走，
        return res

A = Solution()
A.combine(5,2)
print(A.combine(5,2))