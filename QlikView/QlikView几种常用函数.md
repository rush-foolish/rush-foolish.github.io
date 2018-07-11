### *Mapping Load*

> 在qlikview中， mapping只适用于1 to 1 或者 1 to many， 对于一对多的或者多对多的 最好用join的方式

- *ApplyMap*
ApplyMap('map_name', expression [ , default_mapping ] )

*Note*: ApplyMap常被用于获得对应数据值和where筛选条件中，同样被用于where条件中的还有Exists。

```
1. ApplyMap
// Load mapping table for Country Code
Country_Map:
mapping LOAD * 
Inline [
CCode, Country
Sw, Sweden
Dk, Denmark
No, Norway
] ;

//Mapping to the country, If the country code is not in the mapping table, put default value 'Rest of the world'
Salespersons:
LOAD *, 
ApplyMap('Country_Map', CCode,'Rest of the world') As Country 
Inline [
CCode, Salesperson 
Sw, John
Sw, Mary
Sw, Per 
Dk, Preben
Dk, Olle
No, Ole 
Sf, Risttu] ;

//Drop no-needed field
Drop Field 'CCode' from Salespersons;

```
Country | Salesperson
----------------- | ---------
Sweden | John
Sweden | Mary
Norway | Ole
Denmark | Olle
Sweden | Per
Denmark | Preben
Rest of the world | Risttu


- *MapSubString*

替换对应的string, 而map table也只能是1 to 1 或者 1 to many

```
// Load mapping table for Action Desc
Action_Map:
mapping LOAD * 
Inline [
Action, ActionD
read, Read
write, Write
upd, Update
] ;

//Mapping to corresponding Action Desc
Salespersons:
LOAD *, 
MapSubString('Action_Map', Action ) As ActionD 
Inline [
User, Action 
u1, 'write,upd'
u2, 'read,write'
] ;

2. Exists
PtypeFilter:
load * incline [
Ptype
a,
b,
c
]

targ:
load m, n, type
from <File>
Where Exists(Ptype, type)
and WildMatch(m, 'es-*')
and index(n, 'member')>p
;

```

User | Action | ActionD
----- | ------------- | -------------
u1 | write,upd | Write,Update
u2 | read,write | Read,Write


### *JOIN* & *KEEP*

> qlik view中引入Join的概念，类似于普通sql的Join，同时为了便于操作，还引入了类似left keep的函数.
这里需要提一下：qlikview 可利用 --*SQL SELECT/INSERT INTO*-- 来对接到数据库实施query和insert操作， 语法和连接到的数据库类似

##### *Sample:*
*Table1*

A | B
---- | ----
1 | aa
2 | cc
3 | ee

*Table2*

A | C
---- | ----
1 | xx
4 | yy

- *Left Join* 

--Note:数据经过join后，最后只有一张表存在，相当于主表上多拿到了几个fields--

```
Table1:
Load
A, B
FROM Tables;

Left join(Table1)
Load A, C
From Table2;

```
*Result*：

A | B | C
---- | ---- | ----
1 | aa | xx
2 | cc | 
3 | ee | 


- *Left Keep*

--Note:最终会得到两张独立的表，主表不便， 次表只保留能连接上主表的记录

```
Table1:
Load
A, B
FROM Tables;

Left Keep(Table1)
Load A, C
From Table2;

```

*Result*：

A | B
---- | ----
1 | aa
2 | cc
3 | ee

A | C
---- | ----
1 | xx


### *NoOfRows* & *Peek*

> 常被用于loop中，作为收集多个特定的source用

*peek(fieldname [ , row [ , tablename ] ] )*

--Returns the contents of the fieldname in the record specified by row in the internal table tablename. Data are fetched from the associative QlikView database.-- 

```
Load test file from each folder:-

SrcFolder:
Load * 
Inline [
FolderName
'fd1'
'fd2'
'fd3'
'fd3'
] ;

LET RowNum = NoOfRows('SrcFolder');

For vRowNo = 1 to $(RowNum)
	Let vFolderName = 'C:\\Test\' & Peek('FolderName', vRowNo-1, 'SrcFolder');
	Load
		*
	From $(vFolderName)\test.qvd(qvd);
NEXT RowNo

Comments：----------------------------------------------
peek( 'Sales', 0, 'Tab1' ): peek first record from table
peek( 'Sales', 1, 'Tab1' ): peek first second from table
```

