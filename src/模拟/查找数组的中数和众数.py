'''
10 11 21 19 21 17 21 16 21 18 15
'''
arry=list(map(int,input().split()))

dic={}

for i in arry:
    dic[i]=dic.get(i,0)+1
max_num=max(dic.values())
zhongshu=[]
for k,v in dic.items():
    if v ==max_num:
        zhongshu.append(k)
print(zhongshu)
zhongshu.sort()
if len(zhongshu) %2 ==0:
    index=len(zhongshu)//2
    print((zhongshu[index]+zhongshu[index-1])/2)
else:
    print(zhongshu[len(zhongshu)//2])