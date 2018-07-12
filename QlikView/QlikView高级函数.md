## QlikView 高级函数

> QlikView中一些较实用的进阶函数

### 内部表的行列转换

#####  CrossTable-行转列 （turn a cross table into a straight table）

crosstable (attribute field name, data field name [ , n ] ) ( loadstatement | selectstatement )

```SQL

attribute field: the field should be kept as dimension, the column name
data field: the field that contains the attribute value 
n : the first numbers fileds should be kept, something like the below columns - Person, Location 

Crosstable (Month, Sales, 2) LOAD * INLINE[
Person, Location, Jan, Feb, Mar
Bob, London, 100, 200, 300
Kate, New York, 400, 500, 600
];

Somthing Like sql:

select person, Location, 'Jan' as Month, Jan as Sales From table
union 
select person, Location, 'Feb' as Month, Feb as Sales From table
union 
select person, Location, 'Mar' as Month, Mar as Sales From table

```

Result:

Person | Location | Month | Sales
---------- | ------------ | ---------- | ----------
Bob | London | Feb | 200
Bob | London | Jan | 100
Bob | London | Mar | 300
Kate | New York | Feb | 500
Kate | New York | Jan | 400
Kate | New York | Mar | 600


#####  列转行 （turn a cross table into a straight table）

- 可用

```SQL

SUB ReverseCrossTable(vOriginTable, vResultTable)	
//create Generic Table, will create several temp table Genric_Table.Jan, Genric_Table.Feb, Genric_Table.Mar

	Genric_Table:
	Generic LOAD * Resident $(vOriginTable);
/*Genric_Table.Jan
Key,	Jan
Bob,	100
Kate,	400
*/
  
 FOR i=0 to NoOfTables() //Returns the number of tables previously loaded. 
		Tablelist:
		LOAD 
			 TableName($(i)) as Tablename AutoGenerate 1
		Where WildMatch(TableName($(i)), 'Genric_Table.*'); 
    
    //TableName( 'TableNumber' ) Returns the name of the table with the specified number

	NEXT i;

	FOR i=1 to FieldValueCount('Tablename')//Returns the number of distinct values in a field. Fieldname must be given as a string
		LET vTable =  FieldValue('Tablename', $(i)); //Returns the field value found in position n of the field fieldname (by load order)
		
		Left Join($(vResultTable))
		LOAD * 
		Resident $(vTable);
		
		DROP Table $(vTable);
	NEXT i;

	DROP Table Tablelist;

END SUB


Table1:
Generic LOAD * INLINE [
Key, Attribute, Value
Bob, Jan, 100
Bob, Feb, 200
Bob, Mar, 300
Kate, Jan, 400
Kate, Feb, 500
Kate, Mar, 600
];
//below table is to keep the dimension column - key

TargetTable:
Load distinct 
      Key
Resident Table1;

Call ReverseCrossTable('Table1', 'TargetTable');

Result:
Person, Jan, Feb, Mar
Bob, 100, 200, 300
Kate, 400, 500, 600



Something like SQL:

SELECT Key, 
max(case when Attribute='Jan' then Value) as Jan,
max(case when Attribute='Feb' then Value) as Feb,
max(case when Attribute='Mar' then Value) as Mar
FROM Table1
group by Key;

```



