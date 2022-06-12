#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end=' ')
            node = node.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total%10)
            remainder = total//10

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            curr = curr.next

        if remainder : curr.next = ListNode(remainder)
        return result.next


if __name__ == '__main__':
    a = Solution()
    l = LinkList()
    data1 = [1, 2, 3]
    data2 = [2, 4, 6]
    l1 = l.initList(data1)
    l2 = l.initList(data2)
    a.addTwoNumbers(l1,l2)
    # l.printlist(l1)
    # print("\r")
    # l.printlist(l2)
    # print("\r")
    # m = a.mergeTwoLists(l1, l2)