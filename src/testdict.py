

def get_dic():
    str = ['A','B','B','G','G','C','F','F','B']
    dic = {}
    for i in str:
        if i not in dic:
            dic[i] =1
        else:
            dic[i]+=1
    return dic
'''
if 'A' in dic:
    print("true")
else:
    print("flase")
#print(sorted(dic))
'''
def get_val_list(dic):
    val_list = []
    for key,val in dic.items():
        val_list.append(val)
    return val_list




def get_topk(dic):
    key_list= []
    val_list = []
    for key,val in dic.items():
        key_list.append(key)
        val_list.append(val)
    print(key_list)
    print(val_list)
    get_val_index=val_list.index(3)
    print(get_val_index)
    print(key_list[get_val_index])


def get_endlist(val_list):
    for i in range(0,len(val_list)):
        for k in range(0,len(val_list)-1-i):
            if val_list[k+1]>val_list[k]:
                c = val_list[k+1]
                val_list[k+1] = val_list[k]
                val_list[k] = c
    #print(val_list)
    return val_list[0],val_list[1],val_list[2]




'''
list1 = [3, 3, 8, 9, 2, 10, 6, 2, 8, 3, 4, 5, 5, 4, 1, 5, 9, 7, 10, 2]
index_list = [a for a, b in enumerate(list1) if b == 3]
print(index_list)
'''
if __name__ =='__main__':
  get_dic()
  val_list=get_val_list(get_dic())
  get_endlist(val_list)
  print(get_endlist(val_list)[0])

