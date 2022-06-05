'''
描述
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
数据范围：字符串长度满足 1 \le len(str) \le 1000 \1≤len(str)≤1000
输入描述：
一个只包含小写英文字母和数字的字符串。
输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。
示例1
输入：
aaddccdc
复制
输出：
cda
复制
说明：
样例里，c和d出现3次，a出现2次，但c的ASCII码比d小，所以先输出c，再输出d，最后输出a.
'''
# import heapq
# from typing import List
# str1 = input()
# str1=sorted(str1)
# dic ={}
# for i in str1:
#     dic[i]=dic.get(i,0)+1
#
# heap = []
# for k,v in dic.items():
#     heapq.heappush(heap,(v,k))
# res =[0]*len(heap)
# for i in range(len(heap)-1,-1,-1):
# #for i in range(len(heap)):
#     res[i]=heapq.heappop(heap)[1]
#     #dic.values()
# print(res)


while True:
    try:
        a = input()
        s = sorted(set(a))
        ss = sorted(s,key=lambda x:a.count(x),reverse=True)
        print(''.join(ss))
    except:
        break

