#!/bin/bash

# 括号前后要有空格，尤其是表达式，中间没有空格会被解析成一个字符串，表达式被看成字符串就是永真
if [ $  # -lt 2 ]
then
echo xxx.sh 进程名 时间秒
exit
fi

# grep -v 后面接反向过滤的字符串，head拿到grep的第一行（如果很多进程重名），awk打印第二参数，也就是ps的进程号
pid=`ps -ef | grep $1 | grep -v grep | grep -v '/bin/bash' | head  -n 1 | awk '{printf $2}'`

# 变量赋值左边不能有$
tmpfile=${1}_${pid}.tmp

# 判断临时文件是否被创建过，创建过就删除
if[-e $tmpfile]
then
rm -rf $tmpfile
fi

# 创建临时文件
touch ${1}_${pid}.tmp

# 打印一个简单的表头
echo 'timestamp    cpu%' >> $tmpfile

# 持续时间存在remaining_time
remaining_time=$2
while ((remaining_time - -))
    do
# 获取时间
time = `date + % T
`
# top -b -n 1 -c 即打印一次的top
# awk是可以累加每行的，最后打印，多个重名进程可以把它们的CPU加起来
cpu = `top - b - n
1 - c | grep - E $1 | grep - v
grep | awk
'{ sum_cpu+=$9; } END { printf ("%8.2f%", sum_cpu) }'
`
echo $time
'    '$cpu >> $tmpfile
sleep
1
done






#!/bin/bash
pid=$1 #获取进程pid
echo $pid
interval=1 #设置采集间隔
while true
do
echo $(date +"%y-%m-%d %H:%M:%S") >> proc_memlog.txt
cat /proc/$pid/status|grep -e VmRSS >> proc_memlog.txt #获取内存占用
cpu=`top -n 1 -p $pid|tail -2|head -1|awk '{ssd=NF-4} {print $ssd}'` #获取cpu占用
echo "Cpu: " $cpu >> proc_memlog.txt
echo $blank >> proc_memlog.txt
sleep $interval
done



pid=10582  //指定进程id

interval=10 //时间间隔

filename= 'mem_cpu_record.txt'//记录文件名

while true

do

        date "+%Y-%m-%d-%H:%M:%S" | tr '\n' ' ' >>$filename            //记录时间

        cat /proc/$pid/status |grep -e VmRSS   | tr '\n' ' '    >>$filename //记录内存

        top -b -n 1 -p $pid | sed '1,7d' |awk '{print $9}' >>$filename      //记录cpu占用

        sleep $interval

done

https://blog.csdn.net/qq_34465338/category_11775001.html
https://blog.csdn.net/weixin_44028181/article/details/125256546
————————————————
版权声明：本文为CSDN博主「道阻且长,行则将至」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/j99999999955555/article/details/120579935
