## 函数

> 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

```python
a = abs
print(a(-1)) ##1
```

- **定义函数def**

    1. 定义函数时，需要确定函数名和参数个数；
    2. 如果有必要，可以先对参数的数据类型做检查；
    3. 函数体内部可以用return随时返回函数结果；
    4. 函数执行完毕也没有return语句时，自动return None。
    5. 函数可以同时返回多个值，但其实就是一个tuple。

    ```python
    #示例1:
    import math
    def quadratic( a, b, c):
        delt = b**2 - 4 * a * c
        if delt < 0 :
            print('%fx**2 + %fx + %f = 0 无解!'%(a,b,c))
        elif delt == 0:
            print('%fx**2 + %fx + %f = 0 有一个解为 %f'%(a,b,c,-b/(2*a)))
        else:
            x1 = (-b + math.sqrt(delt))/(2*a)
            x2 = (-b - math.sqrt(delt))/(2*a)
            print ('%fx**2 + %fx + %f = 0 的解 为 %f 和 %f'%(a,b,c,x1,x2))

    quadratic(1.3,6.5,4.4)
    
    #示例2：
    def power (x, n = 2):
        s = 1
        while n > 0:
            s = s * x
            n = n - 1
        return s

    print(power(5,3))
    ```

- **参数**  

	1. **可变参数**

	![argument](\_images\arguments1.PNG)

	2. **关键字参数**(利用关键字参数来定义这个函数就能满足注册的需求，必填项和可选项的区别)

	```python
	def person(name, age, **kw):
	    print('name:', name, 'age:', age, 'other:', kw)
	person('R',15) 
	#name: R age: 15 other: {}
	person('M',18,city ='SH')
	# name: M age: 18 other: {'city': 'SH'}
	other = {'city':'bj','gender':'F'}
	person('M',18,**other)
	#name: M age: 18 other: {'city': 'bj', 'gender': 'F'}
	```
	
	> NOTE:可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个**tuple**; 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个**dict**。
	    
	3. **命名关键字参数**: 限制关键字参数的名字,命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
	
	```python
	def person(name, age, *, city, job):
	    print(name, age, city, job)#Jack 24 Beijing Chaoyang
	
	def person1(name, age, *arg, city, job): #形参中有一个可变参数，则分隔符*可以省略
	    print(name,age,arg, city, job) #J 25 (1,) Beijing Chaoyang
	
	person('Jack', 24, city='Beijing', job='Chaoyang')
	person1('J',25,1,city='Beijing',job='Chaoyang')
	```
	
	4. **组合参数**
	
	```python
	def f1(a, b, c=0, *args, **kw):
	    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
	
	f1(1, 2, 3, 'a', 'b', x=99)
	#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
	```
	
   **++对于任意函数，都可以通过类似func(*args, **kw)的形式调用++**

- **递归函数**

    > 在函数内部，可以调用其他函数,使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出

    ![ITER](\_images\iter.PNG)

    ```python
    汉诺塔：
    def move(num, a,b,c):
        if num == 1:
            print('move',a,'->',c)
            return
        move(num-1,a,c,b)
        print('move', a, '->', c)
        move(num-1,b,a,c)
    move(3,'a','b','c')
    ```
