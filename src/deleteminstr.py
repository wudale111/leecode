s = input()
dic = {}
for i in s:
    dic[i] = dic.get(i,0)+1
MIN = min(dic.values())
for i in s:
    if dic[i] == MIN:
        s = s.replace(i,'')
print(s)