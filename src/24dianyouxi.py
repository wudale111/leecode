from typing import List


# 整体想法
#
# 每次选择两个数 把这两个数的计算结果 和之前nums数组中其他元素组成的列表concate起来
# 作为新的nums 向下递归
# 需要注意的细节
#
# 每次是选择两个数，组合、不是排列，不区分\{i, j\}{i,j} 和 \{j,i\}{j,i}，所以我们固定 j>ij>i
# 对选择的两个数字 nums[i]nums[i] 和 nums[j]nums[j] 进行计算的时候，减法和除法注意交换顺序算两次
# 进行除法的时候判断一下除数是否非零
# 只要有一个得到2424了，就返回，所以每次递归判断一下结果，if ~~True, return ~~Trueif  True,return  True
# 由于小数除法有误差 所以最后判断和24的差值是否充分小
# 为了避免代码断行 换了一下函数名


# class Solution:
#     def judgePoint24(self, cards: List[int]) -> bool:
#
#         if len(cards) == 1:
#             return abs(24 - cards[0]) <= 10 ** (-10)
#         # 每次把计算结果 和之前nums数组中其他元素组成的列表concate起来 作为新的nums 向下递归
#         for i in range(len(cards) - 1):
#             for j in range(i + 1, len(cards)):
#                 if self.judgePoint24([cards[i] + cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
#                     return "true"
#                 if self.judgePoint24([cards[i] * cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
#                     return "true"
#                 if self.judgePoint24([cards[i] - cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
#                     return "true"
#                 if self.judgePoint24([cards[j] - cards[i]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
#                     return "true"
#                 if cards[j] != 0 and self.judgePoint24([cards[i] / cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
#                     return "true"
#                 if cards[i] != 0 and self.judgePoint24([cards[j] / cards[i]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
#                     return "true"
#         # 走到这一步 说明之前都不行
#         return "false"
#
#
# A = Solution()
# list = []
# a, b, c, d = map(int, input().split())
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
#
# print(A.judgePoint24(list))

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        if len(cards) == 1:
            return abs(24 - cards[0]) <= 10 ** (-10)
        # 每次把计算结果 和之前nums数组中其他元素组成的列表concate起来 作为新的nums 向下递归
        for i in range(len(cards) - 1):
            for j in range(i + 1, len(cards)):
                if self.judgePoint24([cards[i] + cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
                    return True
                if self.judgePoint24([cards[i] * cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
                    return True
                if self.judgePoint24([cards[i] - cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
                    return True
                if self.judgePoint24([cards[j] - cards[i]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
                    return True
                if cards[j] != 0 and self.judgePoint24([cards[i] / cards[j]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
                    return True
                if cards[i] != 0 and self.judgePoint24([cards[j] / cards[i]] + cards[0:i] + cards[i + 1:j] + cards[j + 1:]):
                    return True
        # 走到这一步 说明之前都不行
        return False
A = Solution()
list = []
a, b, c, d = map(int, input().split())
list.append(a)
list.append(b)
list.append(c)
list.append(d)

print(A.judgePoint24(list))