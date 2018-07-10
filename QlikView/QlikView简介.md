### Qlik View 简介

> QlikView 是一个完整的商业分析软件，使开发者和分析者能够构建和部署强大的分析应用。QlikView 应用使各种各样的终端用户以一个高度可视化，功能强大和创造性的方式，互动分析重要业务信息

#### *特点：*

1. 基于Windows平台

2. 开发使用简单，简单地解决复杂的商业问题

2. 不需要数据仓库 不需要 OLAP 携带方便：不需要特定的基础硬件设施，任何地方都可以共享

3. 含有便利的无缝整合技术：随着你的业务的增长，可以处理大量数据记录

4. 前端交互性比较灵活，展示样式多样化

5. 关联查询功能使其具有独特的数据钻取特性

6. QlikView数据文件(QVD文件)概念的引入，一定程度上取代了ETL工具的功能

7. 支持离线分析

#### *缺点：*

1. 基于内存型的BI工具，数据处理很大程度上依赖内存的大小， 硬件要求较高， 对于内存小数据量大的， 很容易load失败

2. 对于一些复杂逻辑需要写qvs（qlik view script）

3. .qvd文件是一个二进制（Binary）文件，在unix下cat这个文件会呈现一种类似xml格式， 但是不能做grep 等的操作 

4. qlik view 在读取某些非.qvd文件时（csv 或者 txt），会更改某些纯数字字段(字段本身不是纯数字)的值，重新存储到另一个文件时会发生随机变化，
例如 001（test1.csv）-->0001(test2.csv) -->$1(test3.csv)

#### *使用*

1. 可连接到各种关系型数据库
```
ODBC CONNECT TO DB_NAME
```

2. 可调用其他qvs脚本，或者自定义function
```
1. 引入其他脚本
$(Include=filepath\config.qvs)

2.自定义qlikview内部function
Open .qvw file -->Tools -->Edit Module -->type something below in the tab -->Check -->OK

Function addType(istring, pattern)
  set a=...
  for ..
  
END Function
```

3. 对于存储在qv内存中的表， 相同的字段名会自己做连接，如不想连接可以用Noconcatenate 让表不作关联 
具体各表之间的关系，可以查看在Edit Script -->Table Viewer中查看。

4. 对于不使用的临时表，及时Drop，不占用内存

5. 对于主表是大表，left join慎用， 防止data volume 太大引起脚本运行失败
