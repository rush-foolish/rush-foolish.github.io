### BIRT HELP
**What is BIRT**
BIRT is an open source software project that provides the BIRT technology platform to create data visualizations and reports that can be embedded into rich client and web applications, especially those based on Java and Java EE. it's a top-level software project within the Eclipse Foundation...
[**Reference  Documentation...**](http://www.eclipse.org/birt/documentation/install.php)

1. installation
	- download JDK 1.7+
	- download [BIRT Designer](http://download.eclipse.org/birt/downloads)
	- download [customers.rptdesigner](http://www.eclipse.org/birt/documentation/tutorial/tutorial-1.php), save the file(XML) into Eclipse project directory
2. tutorial
	- [video](http://www.eclipse.org/birt/documentation/tutorial/)
	 
3. Palette
`Palette包括以下一些常用的元素：

标签（Label）：标签元素用于显示静态文本，标签元素的外观可以通过本地进行设置，如设置标签元素的超级连接、字体大小等属性；

文本（Text）：文本元素与标签元素相似，只是文本元素可以显示多行数据，更加易于格式输出。可以在文本元素中使用脚本表达式，然后在客户端使用标签进行解析；

动态文本（Dynamic Text）：动态文本元素通常用于显示CLOB数据值。CLOB数据可以通过使用BIRT Expression Builder得到数据；

数据（Data）：数据元素用于显示数据源的数据，通过使用Expression Builder来操作或改变数据值。例如，数据集有包含姓列以及名列，那么可以使用Expression Builder来将姓列与名列进行合并，从而形成包含姓名的一列；

图像（Image）：图片元素用于在报表模板中显示图片。BIRT支持通过URL获得图片，或是从数据库的取得图片（BLOB），或是从本地硬盘上获得图片；

网格（Grid）：网格元素用于布局报表中的报表元素，并进行统一的管理。例如，想在报表中显示产品销售数据表格，同时又想在右边显示一张图表，此时则需要使用Grid来进行网格划分，将报表分成一行两列；

列表（List）：列表元素也相当于一个容器，它不同于其它容器的地方在于列表元素可以绑定到数据集上。列表元素包含头、脚及数据部分。当渲染列表元素时，头与脚部分一次性渲染完成，而中间的数据部分需要显示数据集的每一行数据。数据格式可以是文本元素，也可以是表格、列表等元素；

表（Table）：表格元素与列表元素相似，都可以用于显示数据集中的数据。表格元素与HTML中的表格元素风格相似；

聚合（Aggregation）：汇总元素是BIRT 2.2新增的元素，使用Aggregation Builder向报表添加汇总功能。Aggregation Builder提供的汇总功能大概有25项，常见的如：SUM、MIN、MAX、AVERAGE等等；`

4. Birt Sample
![Birt](/_images/birt sample.png)
