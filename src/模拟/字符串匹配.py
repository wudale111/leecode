import re

while 1:
    try:
        m = input()
        k = input()
        a = re.search(k, m)
        key = a.group()
        if key:
            print(m.index(key) + 1)
        else:
            print(-1)
    except Exception as e:
        break
