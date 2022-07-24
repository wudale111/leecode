


#这里不能用for，因为右指针要停止，左指针收缩，这时候要用while
arry=[1,3,8,1,4,2,5]
target=8
left=0
right=0
max_len=0
while right<len(arry):
    if sum(arry[left:right+1])==target:
        max_len=max(max_len,len(arry[left:right+1]))
        right +=1
        left +=1
    elif sum(arry[left:right+1])>target and left<right:
        left +=1
    elif sum(arry[left:right+1])<target:
        right +=1
    else:
        right +=1
print(max_len)
# for right in range(len(arry)):
#     if sum(arry[left:right+1])==target:
#         max_len=max(max_len,len(arry[left:right+1]))
#     elif sum(arry[left:right+1])>target:
#         left +=1






