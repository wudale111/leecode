import pymysql

conn = pymysql.connect(host='localhost',user = "root",passwd = "root",db = "shop")
#print (conn)
#print (type(conn))
cursor = conn.cursor()
select = cursor.execute('select email from sp_member where id =1')
#print(select)
for line in cursor.fetchall():
    for i in line:
        str =i.split("\n")
        for k in str:
            str = k.split(":")
            list = []
            print(str)
            a = str[1]
            list.append(a)
            #a=list.append(str[1])
            print(list.append(a))


