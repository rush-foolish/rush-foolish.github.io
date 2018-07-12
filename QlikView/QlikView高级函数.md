## QlikView 高级函数

> QlikView中一些较实用的进阶函数

### 1.内部表的行列转换


#####  CrossTable-行转列 （turn a cross table into a straight table）


crosstable (attribute field name, data field name [ , n ] ) ( loadstatement/selectstatement )
	

	```
	/* 
	attribute field: the field should be kept as dimension, the column name
	data field: the field that contains the attribute value 
	n : the first numbers fileds should be kept, something like the below columns - Person, Location 

	*/

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


#####  列转行 （turn a straight table into a cross table ）


	```

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

		FOR i=1 to FieldValueCount('Tablename')
		//FieldValueCount:Returns the number of distinct values in a field. Fieldname must be given as a string
			LET vTable =  FieldValue('Tablename', $(i)); 
			//FieldValue:Returns the field value found in position n of the field fieldname (by load order)

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

### 2.HierarchyBelongsTo

> 一般用于父子关系，找出某个节点(父/子)下所属的所有（子/父）节点

	```
	1.
	HierarchyBelongsTo (NodeID, AncestorID, NodeName, AncestorID, AncestorName, DepthDiff) LOAD * inline [
	NodeID, AncestorID, NodeName
	1, 4, London
	2, 3, Munich
	3, 5, Germany
	4, 5, UK
	5, , Europe 
	//需要注意这里， 在求某节点的所有父节点时， 需要保证最上面和最下面的一个节点是空值，表明这是到达了顶端或低端， 否则关系层级不完整
	];
	
         
	2.针对上面的结果，我们需要人为给一个节点，使树形结构完整
	
	a:
	LOAD * inline [
	NodeID, AncestorID, NodeName
	1, 4, London
	2, 3, Munich
	3, 5, Germany
	4, 5, UK
	];
	//人为制造终极父/子节点
	Concatenate(a)
	load Distinct
		AncestorID as NodeID,
		Null() as AncestorID	
	Resident a;	

	d:
	HierarchyBelongsTo (NodeID, AncestorID, NodeName, AncestorID, AncestorName, DepthDiff)load * Resident a;

	drop table a;

	```

	Result:

NodeID | NodeName | AncestorID | AncestorName | DepthDiff
-------- | ------------ | ------------ | ----------------- | --------
1 | London | 1 | London | 0
1 | London | 4 | UK | 1
1 | London | 5 | Europe | 2
2 | Munich | 2 | Munich | 0
2 | Munich | 3 | Germany | 1
2 | Munich | 5 | Europe | 2
3 | Germany | 3 | Germany | 0
3 | Germany | 5 | Europe | 1
4 | UK | 4 | UK | 0
4 | UK | 5 | Europe | 1
5 | Europe | 5 | Europe | 0
	


