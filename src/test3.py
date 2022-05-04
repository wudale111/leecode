'''
str = ['1','2','4','3','7','6']

for i in range(0,len(str)):
    for k in range(0,len(str)-1-i):
        if str[k+1]<str[k] :
            a = str[k+1]
            str[k+1]=str[k]
            str[k] = a

#print(str)
from testclass import A

a=A()
print (a._string)
#print(A.fun())

'''
# import heapqtest
# a = [1,3,2,7,5,4,9,0]
# b= []
# for i in a:
#     heapqtest.heappush(b, i)
# c= []
# for k in range(len(b)):
#     c.append(heapqtest.heappop(b))
# print(c)

# str = input("输入字符串")
# a= str.split(' ')
# print(a)


# str = input()
# str2 = input()
# class Solution:
#     def nums(self,str,str2):
#         k=0
#         for i in str:
#             if i == str2:
#                 k = k + 1
#         return k
# a = Solution()
# k=a.nums('c','j')
# print(k)



# str = 'abcabc'
# str2 ='a'
# for i in str:
#     if i == str2:
#         print(i)


# heapq.heappush(a,3)
# print(a)
# heapq.heappush(a,5)
# print(a)
# heapq.heappush(a,1)
# print(a)
# # heapq.heappush(a,1)
# a = [2,4,1,3,6,1,4]
# heapq.heappush(a,3)
# print(a)
# heapq.heappush(a,5)
# print(a)
# heapq.heappush(a,1)
#heapq.heapify(a)
#print(a)

#创建并输出链表
# class Node:
#     def __init__(self,value=None,next=None):
#         self.value=value
#         self.next=next
# if __name__ =="__main__":
#     i = 1
#     head = Node(None)
#     head.next = None
#     cur = head
#     while i<9:
#         tmp = Node(i)
#         tmp.next = None
#         cur.next = tmp
#         cur = tmp
#         i += 1
#     print("顺序输出：")
#     cur = head.next
#     while cur is not None:
#         print(cur.value, end=" ")
#         cur = cur.next #结果为1,2,3,4,5,6,7,8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class LinkList:
#     def __init__(self):
#         self.head = None
#
#     def initList(self, data):
#         # 创建头结点
#         self.head = ListNode(data[0])
#         r = self.head
#         p = self.head
#         # 逐个为 data 内的数据创建结点, 建立链表
#         for i in data[1:]:
#             node = ListNode(i)
#             p.next = node
#             p = p.next
#         return r
#
#     def printlist(self, head):
#         if head == None: return
#         node = head
#         while node != None:
#             print(node.val, end=' ')
#             node = node.next
#
#
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
#         dummy = p = ListNode(None)
#         s = 0               # 初始化进位 s 为 0
#         while l1 or l2 or s:
#             # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
#             s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
#             p.next = ListNode(s % 10)       # p.next 指向新链表, 用来创建一个新的链表
#             p = p.next                      # p 向后遍历
#             s //= 10                        # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
#             l1 = l1.next if l1 else None    # 如果l1存在, 则向后遍历, 否则为 None
#             l2 = l2.next if l2 else None    # 如果l2存在, 则向后遍历, 否则为 None
#         return dummy.next   # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点
#
#
# if __name__ == '__main__':
#     a = Solution()
#     l = LinkList()
#     data1 = [1, 2, 3]
#     data2 = [2, 4, 6]
#     l1 = l.initList(data1)
#     l2 = l.initList(data2)
#     l.printlist(l1)
#     print("\r")
#     l.printlist(l2)
#     print("\r")
#     m = a.addTwoNumbers(l1, l2)
#     l.printlist(m)



# class Solution:
#     def jumpFloor(self , n: int) -> int:
#         dp = [0,1]
#     print(dp)
#     # dp[0] = dp[1] = 1
#     # for i in range(2, n + 1):
#     #     dp[i] = dp[i - 1] + dp[i - 2]
#     # return dp[-1]
#
#
#
#
# A = Solution()
# print(A.jumpFloor())

# for i in range(3,3):
#     print(i)
# num = input()
# index,value = map(int, input().split(' '))
# print(index,value)
dp = [0]*1
dp[0] = 1
print(dp[0])



