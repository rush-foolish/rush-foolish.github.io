## Python基础

- **字符串和编码**
    1. ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节（特殊的用4个字符）
    2. 在网页上一般开头用 **<meta charset="UTF-8" />**字样的表示编码方式采用utf-8
    
		![code](\_images\code.PNG)
    
	3. 单个字符编码ord() 和 chr
	    ```python
	    a = chr(90) #Z
	    b = ord('A') #65
	    ```
	
**Note**:纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围

	```python
	1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
	##把str编码为指定bytes
	a = 'ABC'.encode('ascii') #b'ABC'
	
	b = '中文'.encode('utf-8') #b'\xe4\xb8\xad\xe6\x96\x87'
	
	##把指定字符编码变为str
	c = b'ABC'.decode('ascii') #ABC
	
	d = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') #中文
	```
	
- **格式化**

	```python
	print( 'Hi, %s, you have $%d, I just have $%.2f' % ('R', 100,3.14159))
	#Hi, R, you have $100, I just have $3.14
	%d	整数
	%f	浮点数
	%s	字符串
	%x	十六进制整数
	```
	
- **list 和 tuple**

	1. **list**：一种有序的集合，可以随时添加和删除其中的元素，另外list的元素也可是list
		
		```python
		##list基础
		l = ['l1', 'l2', 'l3']
		l1 = l[0] #l1
		l2 = l[-3] #l1
		
		##list后追加元素append
		l.append('other')
		#['l1', 'l2', 'l3', 'other']
		
		##把元素插入到指定的位置 insert
		l.insert(2,'app')
		#['l1', 'l2', 'app', 'l3', 'other']
		
		##删除list的元素 pop
		l.pop() #删除末尾元素
		#['l1', 'l2', 'app', 'l3']
		l.pop(1) #删除指定位置元素*
		#['l1', 'app', 'l3']
		```
	
	2. **tuple**：tuple用（）表示，不可变，当元组中只有一个元素时，一般用(1，)表示，防止python*解读成小括号中的数字1*。**可变的tuple**，如：
	
		```python
		t = ('a', 'b', ['A', 'B'])
		t[2][0] = 'M'
		t[2][1] = 'N'
		print (t)
		#('a', 'b', ['M', 'N'])
		改变的不是tuple，而是list改变了，tuple始终指向了三个元素，只不过第三个元素是list，list本身可变
		```
		
		![tuple1](\_images\tuple1.PNG)    ![tuple2](\_images\tuple2.PNG)
		

- **dict 和 set**

	1. dict : 键-值（key-value）存储，具有极快的查找速度, 如果通过list来查找，必须利用两个list通过对应位置查找，list越大查找越慢，dict示例：
	
		```python
		d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
		d.get('Bob') ##获得bob的值
		d.pop('Bob') ##删除bob 
		
		##相同的key, 以最后出现的为准
		d = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Bob': 77}
		#{'Michael': 95, 'Tracy': 85, 'Bob': 77}
		```
		
		**dict 和list对比**：
		
		dict | list
		:---|:---
		查找和插入的速度极快，不会随着key的增加而变慢| 需要占用大量的内存，内存浪费多
		查找和插入的时间随着元素的增加而增加| 占用空间小，浪费内存很少
		
	2. set : set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key,重复的会自动过滤
		
		```python
		s1 = set([1, 2, 3])
		s1.add(4) ##添加
		s1.remove(4) ##删除
		s2 = set([2, 3, 4])
		
		print (s1&s2) ## 交集{2, 3}
		print(s1|s2) ##合集{1, 2, 3, 4}
		# print(s1[0]) ##不支持index，因为set无序
		
		#set也是不可变对象,但是放入list 后，就变成多维list
		s = ([1,2],[2,3])
		s[1][0]
		print(s[1][0]) ##2
		
		s3 = ([1,[2,3]]) #[1, [2, 3]]
		print (s3[0]) #1
		```
	
- **str** ： 是不可变对象,不可变对象调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回

	```python
	a = 'abc'
	b = a.replace('a','A')
	print(a) #'abc'
	print(b) #'Abc',不改变原有的，创建了一个新的对象并返回
	```
	
- **判断语句if**

	```python
	s = input('please input the weight:')
	w = int(s)
	if w < 18 :
	    print ("light")
	elif w > 22:
	    print("heavy")
	else:
	    print ("normal")
	```
	
 - **循环**

	1. for ： for x in ...
		
		 ```python
		names = ['Bart', 'Lisa', 'Adam']
		for name in names:
		    print(name)
		 ```
		
	2. while : 
		
		 ```
		#break
		n = 1
		while n <= 100:
		if n > 10: # 当n = 11时，条件满足，执行break语句
		    break # break语句会结束当前循环
		print(n)
		n = n + 2
		print('END')
		
		#continue
		n = 1
		while n <= 10:
		n = n + 1 # continue 时，增加的步长应写在前面， 否则可能导致死循环
		if n % 2 == 1: #当n 奇数时，条件满足，执行continue
		    continue
		print(n)
		 ```
		
	
