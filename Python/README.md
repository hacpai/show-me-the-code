## Python 练习册

**第 0000 题：**提交 Python 程序，将 Hello World 两个单词分别输出到相邻的两行。（注意：每个单词后面没有空格）

**第 0001 题：**身体质量指数（Body Mass Index，BMI）是根据人的体重和身高计算得出的一个数字，BMI对大多数人来说，是相当可靠的身体肥胖指标，其计算公式为：BMI = Weight/High^2，其中体重单位为公斤，身高单位为米。编写程序，提示用户输入体重和身高的数字，输出BMI。

**第 0002 题：**接收用户输入的一个秒数（非负整数），折合成小时、分钟和秒输出。

**第 0003 题：**对于三角形，三边长分别为a, b, c，给定a和b之间的夹角C，则有：c^2 = a^2+b^2-2axbxcos(C)。编写程序，使得输入三角形的边a, b, c，可求得夹角C(角度值)。

**第 0004 题：**如果列出10以内自然数中3或5的倍数，则包括3,5,6,9。那么这些数字的和为23。要求计算得出任意正整数n以内中3或5的倍数的自然数之和。

**第 0005 题：**10以内的素数2,3,5,7的和为17。要求计算得出任意正整数n以内的所有素数的和。

**第 0006 题：**根据下列信息计算在1901年1月1日至2000年12月31日间共有多少个星期天落在每月的第一天上？

- a)  1900.1.1是星期一
- b)  1月，3月，5月，7月，8月，10月和12月是31天
- c)  4月，6月，9月和11月是30天
- d)  2月是28天，在闰年是29天
- e)  公元年数能被4整除且又不能被100整除是闰年
- f)  能直接被400整除也是闰年

**第 0007 题：**数字197可以被称为循环素数，因为197的三个数位循环移位后的数字：197,971,719均为素数。100以内这样的数字包括13个，2,3,5,7,11,13,17,31,37,71,73,79,97。要求任意正整数n以内一共有多少个这样的循环素数。

**第 0008 题：**一个斐波那契数列的前10项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89，对于一个最大项的值不超过n的斐波那契数列，求值为偶数的项的和。

**第 0009 题：**若已知1800年1月1日为星期3，则对于一个给定的年份和月份，输出这个月的最后一天是星期几。

**第 0010 题：**如在汉诺塔游戏中，我们希望将塔A上的n个盘子，通过塔B移动到塔C，则对于任意输入的n，给出移动的步骤。

**第 0011 题：**“Pig Latin”是一个英语儿童文字改写游戏。

整个游戏遵从下述规则：

(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音字母。其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。

(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。例如，“ask”变为“askhay”，“use”变为“usehay”。

(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。

(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。

(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。 

**第 0012 题：**依次判断一系列给定的字符串是否为合法的 Python 标识符。

**第 0013 题：**依次计算一系列给定字符串的字母值，字母值为字符串中每个字母对应的编号值（A对应1，B对应2，以此类推，不区分大小写字母，非字母字符对应的值为0）的总和。例如，Colin 的字母值为 3 + 15 + 12 + 9 + 14 = 53

**第 0014 题：**定义一个 prime() 函数求整数 n 以内（不包括n）的所有素数（1不是素数），并返回一个按照升序排列的素数列表。使用递归来实现一个二分查找算法函数bi_search()，该函数实现检索任意一个整数在 prime() 函数生成的素数列表中位置（索引）的功能，并返回该位置的索引值，若该数不存在则返回 -1。

**第 0015 题：**帕斯卡三角形，又称杨辉三角形是二项式系数在三角形中的一种几何排列。帕斯卡三角形通常从第0行开始枚举，并且每一行的数字是上一行相邻两个数字的和。在第0行只写一个数字1，然后构造下一行的元素。将上一行中数字左侧上方和右侧上方的数值相加。如果左侧上方或者右侧上方的数字不存在，用0替代。下面给出6行的帕斯卡三角形：

```
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1
```
编写程序，输入帕斯卡三角形的高度 n，然后生成和上面例子一样风格的三角形。

**第 0016 题：**倒排索引（Inverted index），也常被称为反向索引，是一种索引方法，用来存储某个单词存在于哪些文档之中。是信息检索系统中最常用的数据结构。通过倒排索引，可以根据单词快速获取包含这个单词的文档列表。

本作业主要完成以下四个功能：

(1). 建立索引：首先输入100行字符串，用于构建倒排索引，每行字符串由若干不含标点符号的、全部小写字母组成的单词构成，每个单词之间以空格分隔。依次读入每个单词，并组成一个由<单词, 每个单词出现的行号集合>构成的字典，其中行号从1开始计数。

(2). 打印索引：按照字母表顺序依次输出每个单词及其出现的位置，每个单词出现的位置则按行号升序输出。例如，如果“created”出现在第3, 20行，“dead”分别出现在14, 20, 22行。则输出结果如下（冒号和逗号后面都有一个空格，行号不重复）：

    …
    created: 3, 20
    dead: 14, 20, 22
    …

(3). 检索：接下来输入查询(Query)字符串，每行包含一个查询，每个查询由若干关键字(Keywords)组成，每个关键字用空格分隔且全部为小写字母单词。要求输出包含全部单词行的行号（升序排列），每个查询输出一行。若某一关键字在全部行中从没出现过或没有一行字符串包含全部关键字，则输出“None”。遇到空行表示查询输入结束。如对于上面创建的索引，当查询为“created”时，输出为“3, 20”；当查询为“created dead”时，输出为“20”；当查询为“abcde dead”时，输出为“None”；

(4). 高级检索：当输入的Query以“AND: ”开始，则执行“与”检索，即要求输出包含全部关键字的行；如果输入的Query以“OR:”开始，则执行“或”检索，即某行只要出现了一个关键字就满足条件。默认情况（不以“AND: ”或“OR: ”开始），执行“与”检索。

**输入格式:**

首先输入100行字符串，每行字符串由若干不含标点符号的、全部小写字母组成的单词构成，每个单词之间以空格分隔。
若干个查询，每个查询占一行，既可能是普通检索，也可能是高级检索。

**输出格式：**

首先打印索引，然后将每个查询的结果输出到一行。

**第 0017 题：**实现逆向最大匹配分词算法，即从右向左扫描，找到最长的词并切分。如句子“研究生命的起源”，逆向最大匹配分词算法的输出结果为“研究 生命 的 起源”。

**输入格式:**

第一行是以utf-8格式输入的词表，每个词之间以空格分隔。
接下来是若干行以utf-8格式输入的中文句子。

**输出格式：**

以utf-8格式输出的逆向最大匹配的分词结果，每个词之间使用空格分隔。每个输入对应一行输出。

**输入样例：**

你 我 他 爱 北京 天安门 研究 研究生 命 生命 的 起源
研究生命的起源
我爱北京天安门

**输出样例：**

研究 生命 的 起源
我 爱 北京 天安门

**第 0018 题：**两位整数相乘形成的最大回文数是 9009 = 99 × 91。编写程序，求得任意输入的 n 位整数相乘形成的最大回文数。

**输入格式:**
正整数 n 
 
**输出格式：**
n 位整数相乘形成的最大回文数
 
**输入样例：**
2
 
**输出样例：**
9009

**第 0019 题：**用 Tkinter 写一个如图的 GUI 程序，要求单击按钮能改变文本的颜色和边界形式，按键盘方向键画布上的图形能改变大小。

![](http://ww1.sinaimg.cn/large/8178ba0egw1eojroehdo1j208v0brwer.jpg)

**第 0020 题：**建立 splite 数据库，创建 student 表格，表格中有以下数据

id  | name   | room  | tel     
--- | ------ | ----- | --------      
666 | zhan   | 6-303 | 83272451 
777 | zhang  | 6-404 | 83423567 
888 | zhuang | 6-505 | 83256673 

在 Python 中使用 sqlite，并且实现参数化查询，即当输入一个 name 时，显示 name 的相关信息。

**第 0021 题：**用 Django Web 开发框架搭建一个本地的 Web 站点并且编写 Django 应用，在不同 url  下完成以下功能：

1. `/hello` 对任意 Request 返回 "Hello world"
2. `/time`  运用模板动态显示 "现在的时间是..."
3. `/insert` 创建模型，安装数据库，以表单的形式要求用户填入联系人的 name, sex, phone, email, address 并且在 Python 中获得输入的内容插入于数据库中
4. `/list` 在网页上显示联系人信息

**第 0022 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

**第 0023 题：**遍历 names.txt 文件，输出长度最长的回文人名。

**第 0024 题：**Write a function that draws a grid like the following:

```
+ - - - -  + - - - -  +
|          |          |
|          |          |
|          |          |
|          |          |
+ - - - -  + - - - -  +
|          |          |
|          |          |
|          |          |
|          |          |
+ - - - -  + - - - -  +
```

And write a function that draws a similar grid with four rows and four  columns.

**第 0025 题：**用 Swampy 包中的 TurtleWorld 模块画如图所示的花的形状。
![](http://ww2.sinaimg.cn/large/8178ba0egw1eova6ruzltj20jp04zjrp.jpg)

**第 0026 题：**Fermat’s Last Theorem says that there are no integers a, b, and c such that

![](http://ww1.sinaimg.cn/large/8178ba0egw1eow35k15suj20ju02tdfp.jpg)

- Write a function named `check_fermat` that takes four parameters—a, b, c and n—and that checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that

![](http://ww1.sinaimg.cn/large/8178ba0egw1eow36kxcmrj20je01kq2p.jpg)

the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

- Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.

**第 0027 题：**If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. 

1. Write a function named `is_triangle` that takes three integers as arguments,and that prints either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks with the given lengths.
2. Write a function that prompts the user to input three stick lengths, converts them to integers, and uses `is_triangle` to check whether sticks with the given lengths can form a triangle.
