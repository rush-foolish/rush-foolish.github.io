## Shell进程

> 在类Linux环境下,为了便于查看cpu的使用情况可用**top**实时监测，也可利用ps -ef 查看详细的进程

### 查看相关进程

```bash
1. ps -ef | grep "related info" | grep -v grep
#通过related info查找对应的进程信息，并避免匹配到grep 进程

2. ps -ef | awk -F " " '/[I]nformation/{print $2}'
#匹配的得到第二个参数,[]是为了避免匹配到 awk自身进程

3. pgrep -f 'name'
or pgrep -U 'uid'....
#进程自带匹配命令，详细的可查看man pgrep

```

### 结束相关进程

```
1. pkill -f 'name'
or pkill -U 'uid'
# kill相关的进程

2. 编写脚本 kill对应的进程
process=$1
# find the pid which is matched to the condition
pid=`ps -ef |grep $process | grep -v grep | awk -F " " '{print $2}'`

for prc in $pid
do
    # for each process, check if the pid exists currently, and if it is current process which is running
    if [ $prc -ne $$ ]
    then 
        echo "the process_id: $prc"
        kill -9 $prc
    fi  
done

```

