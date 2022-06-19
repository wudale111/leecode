'''
1.新员工考试
小聪入职新公司，参加线上的新员工必备考试，考试共25题，以此是10个判断题（每题2分）、10个单选题（每题4分）和5个多选题（每题8分），总分100分。

考题只能顺序作答，答对题目获得相应分数，答错题目获得0分，考试系统不提示作答是否正确，答题过程中如果累积有3题答错，直接中止考试并计算考试分数。

小聪考试结果是N分（0<=N<=100），请根据小聪的分数，算出所有可能的答题情况的个数。

输入

整数，表示小聪的考试得分N，N为偶数，0<=N<=100（N不会是不可能考出来的分数）。

输出

整数 表示所有可能的答题情况的个数

'''


class Solution:
    def employexam(self,target):
        res=0
        def dfs(sumScore,order,wrongNum,res,target):
            if (sumScore == target):
                res +=1
                return
            if (wrongNum >= 3 or order > 25):
                return
            if (order <= 10):
                dfs(sumScore+2, order+1, wrongNum, 0,target)
                dfs(sumScore, order+1, wrongNum+1,0, target)
            elif order <= 20:
                dfs(sumScore+4, order+1, wrongNum, 0,target)
                dfs(sumScore, order+1, wrongNum+1, 0,target)
            else:
                dfs(sumScore + 8, order + 1, wrongNum,0, target)
                dfs(sumScore, order + 1, wrongNum + 1, 0,target)
        dfs(0,1,0,0,target)
        return res
A=Solution()
target = 94
A.employexam(target)
print(A.employexam(target))
