
arry=input().split(',')
print(arry)
max_len=0
for i in range(len(arry)-1):
    for j in range(i+1,len(arry)):
        if len(arry[i])+len(arry[j])==len(''.join(set(arry[i]+arry[j]))):
            max_len=max(max_len,len(arry[i])*len(arry[j]))
print(max_len)

