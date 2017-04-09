### Python 简介

> Python是著名的“龟叔”Guido van Rossum在1989年圣诞节期间，为了打发无聊的圣诞节而编写的一个编程语言

**Python从规范到解释器都是开源的，可以自己编写，也可以用现在比较流行的,不同的解释器执行结果可能不同**

1. CPython：解释器是C语言开发，使用最广，一般用“>>>”作为提示符
2. IPython：基于Cpython之上的一个交互式解释器，交互式上有所增强，执行是和CPython一样的，用“In[num]”作为提示符
3. PyPy：PyPy采用[JIT技术](https://en.wikipedia.org/wiki/Just-in-time_compilation)，对Python代码进行动态编译（注意不是解释），可以显著提高Python代码的执行速度
4. Jython：运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行
5. IronPython：和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。

**通过命令python 进入交互模式 和 直接运行./xx.py文件的区别：**

- 直接python交互模式，相当于启动Python解释器，但是等待你一行一行输入源代码，每输入一行就执行一行
- 直接运行.py文件相当于启动解释器，并一次性把文件中的代码给执行了，但是需要加

 ```
#!/usr/bin/env python3
# -*- coding：utf-8 -*- 编码
 ```

### Python 基础
- 输入：input
- 输出：print

```
name = input()
print('hello ',name)
```

- **数据类型**

    1. 整数和浮点数：整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（包括除法），而浮点数运算可能会有四舍五入的误差

    ```
    print (10/3)
    3.3333333333333335
    print(10//3)
    3
    print(10%3)
    1
    ```

    2. **字符串**：以单引号'或双引号"括起来的任意文本，''' '''表示多行内容，\为转义字符,示例如下

    ```
    print ('I\'m ok')
    #I'm ok
    print("I'm \"OK\"")
    #I'm "OK"
    print('''
    line
    line2
    line3
    ''')
    #line1
    #line2
    #line3
    ##多行字符串，在前面加 r##
    s1 = r'Hello, "Bart"'
    s2 = r'''Hello,
    Lisa!'''
    print(s1)
    # Hello, "Bart"
    print(s2)
    # Hello,
    # Lisa!
    ```

    3. 布尔值：true/false（进行逻辑运算后的结果，可用and，or，not进行运算）
    4. **空值 none**: 特殊的字符
    5. **变量**：变量名必须是大小写英文、数字和_的组合，且不能用数字开头:

    ```
    a = 'ABC' #解释器创建了字符串'ABC'和变量a，并把a指向'ABC'
    b = a #解释器创建了变量b，并把b指向a指向的字符串'ABC'
    a = 'XYZ' ##解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改
    ```

    ![a](\_images\st1.PNG)
    ![b](\_images\st2.PNG)
    ![ab](\_images\st3.PNG)
