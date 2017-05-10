## SSH (Secure Shell)

> SSH为建立在应用层和传输层基础上的安全协议,是目前较可靠，专为远程登录会话和其他网络服务提供安全性的协议。几乎所有类**LINUX**平台（在**Windows**平台较多使用**PUTTY**软件）都可使用SSH协议，它可有效防止远程管理过程中的信息泄露问题。

### ssh 基本用法

```bash
＃连接
ssh -p 22 user@host

"-p 22 : portnumber 22"
"user@host: 分配的用户名@远程登录服务器主机的host"

#本地和远程之间文件的复制
scp -P1433 localfile rachel@114.215.236.49:cloudfile
scp -P1433 远程用户名@IP 地址: path/文件名 localfile

#远程连接数据库
mysql -u username -p -h hostip

```

### ssh的处理过程

1. 远程主机收到用户的登录请求，把自己的公钥发给用户。
2. 用户使用这个公钥，将登录密码加密后，发送回来。
3. 远程主机用自己的私钥，解密登录密码，如果密码正确，就同意用户登录

**在每次登陆时，可用公钥登录，省去每次登陆需要输入密码的麻烦**

### 通过公钥登录远程

- 本地
 
```bash
$ ssh-keygen -t rsa

-t:type
```

![ssh_keygen](\_images\ssh_keygen.png)

- 远程服务器端

将本地~/.ssh/**id_rsa.pub**的内容粘贴到**远程服务器的当前目录的.ssh/authorized-keys**文件中(远程中.ssh需要创建)，创建好后利用下面命令更改目录及文件的权限

```bash
$ chmod 700 .ssh
$ chmod 650 .ssh/authorized_keys 
```
退出远程系统再次登录，即可免密码登录，查看当前目录下的known_hosts文件，里面已被添加远程服务器的登录信息

![known_hosts](\_images\known_hosts.png)
