### input语句里面的特殊符号用法总

特殊符号 | 用法
:------------------------|:----------------------------------
$ | 表示变量是字符串
:$10. |  这里的冒号，表示input读取到下一个空格, 或者读完10个字符, 或者本行读取完成时停止
& |表示读取数据到遇到两个连续空格, 或者读完变量定义长度的个字符, 或者本行读取完成时停止, 计入两字符间的空格
@前置 | 表示读取数据时的列绝对指针: @10,表示列指针跳到10的位置（指针从1开始而不是0开始,这里的10也可以是变量名或者表达式)；@'str'表示列指针跳到字符串“str”的紧跟的列位置
@单尾随 | 表示多个input读取同一个数据行的数据
@@双尾随 | 表示一个input在同一行读取多组数据
+和-修饰符 | 表示读取数据时的相对列指针，+n表示指针向右移n个列，-n表示指针向左移n个列
#修饰符 | 表示读取数据时的行相对指针。#2表示行指针跳到当前行后第2行开始位置
\ 修饰符 | 表示行指针跳到当前行下一行开始位置（与#2等同）

- **示例1**

```
data user;                             
a=15;                                  
input age 32-33 @;                       
input  @1 name & $13. +4 addr :$10. @'from=' from $10. @(a*2) sex $ ;

datalines;                            
xiao shucheng  ----chongqing f 23 from=chengdu 
liu ming  ----nanjing        m 25 from=guangzhou 
lishu                                   
;    

proc print;                             
run;  
```

![res1](\_images\clipboard.png)

- **示例2**

```
data user (drop = a );         

a=15;                                 
input name & $13. +4 addr :$10. @'from=' from $10. @(a*2) sex $  #2 school  $20. ;  

datalines;                               
xiao shucheng  ----chongqing f from=chengdu   
重庆大学                              
liu ming  ----nanjing        m from=guangzhou  
兰州大学                              
;                                                                                               
proc print;                             
run;             
```

![res2](\_images\clipboard1.png)

- **示例3**

```
data user;                             
a=15;                                  
input name & $13. +4 addr :$10. @'from=' from $10. @(a*2) sex $ ;
input school & $20. @;                    
input @'age=' age 2. ;                                                                                                                  
datalines;                             
xiao shucheng  ----chongqing f from=chengdu  
重庆大学  age=23                          
liu ming  ----nanjing        m from=guangzhou   
兰州大学  age=26                           
;                                                                                                                                       
proc print;                              
run;
```

![res3](\_images\clipboard2.png)

- **示例4**

```
data user;
input x y @@ ;
datalines;
12 13 14 25 46 78 45 56
;
proc print;
run;
```

![res4](\_images\clipboard3.png)


