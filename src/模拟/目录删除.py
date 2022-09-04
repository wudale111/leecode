while 1:
    try:
        num = int(input())
        lst = []
        tree = {}
        for _ in range(num):
            child, parent = input().split()
            if parent in tree:
                tree[parent].append(child)
            else:
                tree[parent] = [child]
            lst.append((child, parent))
            print(tree,'111')
            print(lst,'222')

        def del_child(parent_id):
            if parent_id in tree:
                for child_id in tree.pop(parent_id):
                    lst.remove((child_id, parent_id))
                    #递归删除改父目录ID下的子目录
                    del_child(child_id)

        del_id = input()
        #这个函数用来删除子目录
        del_child(del_id)

        for c in lst:
            #子目录ID不等于要删除的目录ID，则打印
            if c[0] != del_id:
                print(" ".join(c[0]))

    except Exception:
        break
