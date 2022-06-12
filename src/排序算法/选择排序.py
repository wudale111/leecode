def select_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index !=i:
            arr[i], arr[min_index]=arr[min_index],arr[i]
    return arr

if __name__ == '__main__':
    arr = [10,6,4,11,15,3,7,2]
    print(select_sort(arr))

# def select_sort(arry):
#     n = len(arry)
#     for i in range(len(arry)-1):
#         max_index=i
#         for j in range(i+1,len(arry)):
#             if arry[j]>arry[max_index]:
#                 max_index=j
#         if max_index !=i:
#             arry[i],arry[max_index]=arry[max_index],arry[i]
#     return arry
#
# if __name__ == '__main__':
#     arr = [10,6,4,11,15,3,7,2]
#     print(select_sort(arr))

