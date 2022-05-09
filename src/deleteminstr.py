'''
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
数据范围：输入的字符串长度满足 1 \le n \le 20 \1≤n≤20  ，保证输入的字符串中仅出现小写字母
'''

s = input()
dic = {}
for i in s:
    dic[i] = dic.get(i,0)+1
MIN = min(dic.values())
for i in s:
    if dic[i] == MIN:
        s = s.replace(i,'')
print(s)