## Mysq连接及编码问题

### Mysql 连接

> 安装好后，可将mysql的启动放入 alias 文件

```vim
## login Mysql and server start/stop
alias mysql='/usr/local/mysql/bin/mysql'
alias mysqlstart='sudo /usr/local/mysql/support-files/mysql.server start'
alias mysqlstop='sudo /usr/local/mysql/support-files/mysql.server stop'
```
由于在数据库插入处理时，需要对某些用户进行授权，这时不得不用root登陆进行grant，但由于我长时间没用mysql，忘记密码。用了如下方法找回：

```bash
$ cd /usr/local/mysql/bin/

$ sudo su

$ ./mysqld_safe --skip-grant-tables &
作用是跨过权限验证

$ ./mysql -uroot 
免密码登陆

mysql> use mysql;

mysql> flush privileges
获取权限

mysql> set password for 'root'@'localhost'=password('new password')

退出再次登入,检查是否成功
$ mysql -u root -p
password:
...
mysql> select user();
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
```


### Mysql编码

> 在抓取网站数据的时候, 通常会遇到中文字符插入表中乱码的情况，但是打印出来或者写到文本时没有问题，这时需要检查下mysql表，数据库引擎或者特定字段等的charset设置(查看是否是utf-8，目前基本涵盖全部的字符)。

#### Mysql存入数据和取出数据的过程

1. 存入数据
    
    - 在terminal中使用输入法输入
    - terminal根据字符编码转换成二进制流(如python 爬取网页需要将字节码解码成字符串)
    - 二进制流通过MySQL客户端(client)传输到MySQL Server
    - Server通过character-set-client解码
    - 判断character-set-client和目标表的charset是否一致
    - 如果不一致则进行一次从client-charset到table-charset的一次字符编码转换
    - 将转换后的字符编码二进制流存入文件中

2. 取出数据
    
    - 从文件读出二进制数据流
    - 用表字符集编码进行解码
    - 将数据转换为character-set-client的编码
    - 使用character-set-client编码为二进制流
    - Server通过网络传输到远端client
    - client通过bash配置的字符编码展示查询结果

### 乱码解决方案

1. 查看python的默认连线语系，**#-\*- coding:utf-8 -\*-**
2. 查看mysql server/client本身有无问题
3. db/table/column的语系设定

- 进入数据库，查看状态

```bash
mysql -u root -p

mysql>  show variables like '%char%';
+--------------------------+--------------------------------------------------------+
| Variable_name            | Value                                                  |
+--------------------------+--------------------------------------------------------+
| character_set_client     | latin1                                                   |
| character_set_connection | utf8                                                   |
| character_set_database   | latin1                                                   |
| character_set_filesystem | binary                                                 |
| character_set_results    | utf8                                                   |
| character_set_server     | latin1                                                   |
| character_set_system     | utf8                                                   |
| character_sets_dir       | /usr/local/mysql-5.5.40-osx10.6-x86_64/share/charsets/ |
+--------------------------+--------------------------------------------------------+

mysql> show create table test3;
| test3 | CREATE TABLE `test3` (
  `s1` varchar(20) DEFAULT NULL,
  `s2` varchar(20) DEFAULT NULL,
  `s3` varchar(20) DEFAULT NULL,
  `s4` varchar(20) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
```

针对以上情况：

1.只想针对某个表或者某个字段进行charset 设置，可以和在ddl时设定

```sql
CREATE TABLE `test3` (
  `s1` varchar(20) DEFAULT NULL,
  `s2` varchar(20) DEFAULT NULL,
  `s3` varchar(20) DEFAULT NULL,
  `s4` varchar(20) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |

or s2 need to set the character

CREATE TABLE `test3` (
  `s1` varchar(20) DEFAULT NULL,
  `s2` varchar(20) DEFAULT NULL character set utf8,
  `s3` varchar(20) DEFAULT NULL,
  `s4` varchar(20) DEFAULT NULL,
)
```

2.更改某个整个db的character

```bash
mysql> alter database test character set utf8
mysql>  show variables like '%char%';
+--------------------------+--------------------------------------------------------+
| Variable_name            | Value                                                  |
+--------------------------+--------------------------------------------------------+
| character_set_client     | latin1                                                   |
| character_set_connection | utf8                                                   |
| character_set_database   | utf8                                                   |
| character_set_filesystem | binary                                                 |
| character_set_results    | utf8                                                   |
| character_set_server     | latin1                                                   |
| character_set_system     | utf8                                                   |
| character_sets_dir       | /usr/local/mysql-5.5.40-osx10.6-x86_64/share/charsets/ |
+--------------------------+--------------------------------------------------------+
```

3.整体一次性更改，以后创建任何db／table的时候默认为utf8

- 首先停止当前的mysql sever,切换到root，更改my.cnf文件

```bash
$ mysqlstop
$ sudo su
$ cp /usr/local/mysql/support-files/my-medium.cnf /etc/my.cnf

$ vim /etc/my.cnf
....
# MySQL clients
[client]
...
## add the newline below
default-character-set = utf8

# The MySQL server
[mysqld]
...
## add the newline below
character-set-server = utf8
```

- 修改完成后，重新启动mysql（mysqlstart）,查看当前字符设置

```
mysql>  show variables like '%char%';
+--------------------------+--------------------------------------------------------+
| Variable_name            | Value                                                  |
+--------------------------+--------------------------------------------------------+
| character_set_client     | utf8                                                   |
| character_set_connection | utf8                                                   |
| character_set_database   | utf8                                                   |
| character_set_filesystem | binary                                                 |
| character_set_results    | utf8                                                   |
| character_set_server     | utf8                                                   |
| character_set_system     | utf8                                                   |
| character_sets_dir       | /usr/local/mysql-5.5.40-osx10.6-x86_64/share/charsets/ |
+--------------------------+--------------------------------------------------------+
```

