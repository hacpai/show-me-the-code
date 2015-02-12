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

**第 0028 题：**The Koch curve is a fractal that looks something like Figure.

![](http://ww3.sinaimg.cn/large/8178ba0ejw1eowd9sie65j20jr049jrd.jpg)

To draw a Koch curve with length x, all you have to do is

1. Draw a Koch curve with length x/3. 
2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.
4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.
6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

1. Write a function called `koch` that takes a turtle and a length as parameters, and that uses the
turtle to draw a Koch curve with the given length.
2. Write a function called `snowflake` that draws three Koch curves to make the outline of a snowflake.

**第 0029 题：**The Ackermann function, A(m, n), is defined:

![](http://ww4.sinaimg.cn/large/8178ba0ejw1eowjour35sj20jq03i0sr.jpg)

Write a function named ack that evaluates Ackermann’s function. Use your function to evaluate ack(3, 4), which should be 125. What happens for larger values of m and n?

**第 0030 题：**A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. **Recursively**, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

Write a function called `is_palindrome` that takes a string argument and returns True if it is a palindrome and False otherwise.

**第 0031 题：**The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is Euclid’s algorithm, which is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.

Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

Credit: This exercise is based on an example from Abelson and Sussman’s Structure and Interpre- tation of Computer Programs.

**第 0032 题：**The built-in function eval takes a string and evaluates it using the Python interpreter. For example:

```
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<type 'float'>
```

Write a function called `eval_loop` that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.

It should continue until the user enters 'done', and then return the value of the last expression it evaluated.

**第 0033 题：**Write a function `square_root` using Newton's method.

To test the square root algorithm in this chapter, you could compare it with math.sqrt. Write a function named `test_square_root` that prints a table like this:

![](http://ww1.sinaimg.cn/large/8178ba0ejw1eoxe7st1m7j20jx06rq3o.jpg)

The first column is a number, a; the second column is the square root of a computed with the function `square_root`; the third column is the square root computed by `math.sqrt`; the fourth column is the absolute value of the difference between the two estimates.

**第 0034 题：**The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of π:

![](http://ww4.sinaimg.cn/large/8178ba0ejw1eoxgcpyz8bj20jy02hdfs.jpg)

Write a function called `estimate_pi` that uses this formula to compute and return an estimate of π. It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.

**第 0035 题：**ROT13 is a weak form of encryption that involves “rotating” each letter in a word by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.

Write a function called `rotate_word` that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string “rotated” by the given amount.

For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.

You might want to use the built-in functions ord, which converts a character to a numeric code, and chr, which converts numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13.

**第 0036 题：**Write a function called `nested_sum` that takes a nested list of integers and add up the elements from all of the nested lists.

**第 0037 题：**write a function named `capitalize_nested` that takes a nested list of strings and returns a new nested list with all strings capitalized.

**第 0038 题：**The (so-called) Birthday Paradox:

1. Write a function called `has_duplicates` that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

2. If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.

**第 0039 题：**Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?

Hint: use the time module to measure elapsed time.

**第 0040 题：**To check whether a word is in the word list, you could use the in operator, but it would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary. You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. If so, then you search the first half of the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will take about 17 steps to find the word or conclude that it’s not there.

Write a function called bisect that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not.

Or you could read the documentation of the bisect module and use that!

**第 0041 题：**Two words are a “reverse pair” if each is the reverse of the other. Write a program that finds all the reverse pairs in the word list.

**第 0042 题：**Two words “interlock” if taking alternating letters from each forms a new word. For example, “shoe” and “cold” interlock to form “schooled.”

1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the first, second or third?

**第 0043 题：**Memoize the Ackermann function from Problem 0029 and see if memoization makes it possible to evaluate the function with bigger arguments.

**第 0044 题：**Read the documentation of the dictionary method setdefault and use it to write a more concise version of `invert_dict`. 

**第 0045 题：**If you did Problem 0038, you already have a function named `has_duplicates` that takes a list as a parameter and returns True if there is any object that appears more than once in the list.

Use a dictionary to write a faster, simpler version of `has_duplicates`.

**第 0046 题：**Two words are “rotate pairs” if you can rotate one of them and get the other (see `rotate_word` in Problem 0035).

Write a program that reads a wordlist and finds all the rotate pairs.

**第 0047 题：**Write a funciton that ties are broken by comparing words, so words with the same length appear in reverse alphabetical order. For other applications you might want to break ties at random.

Modify previous function so that words with the same length appear in random order. Hint: see the random function in the random module.

**第 0048 题：**Write a function called `most_frequent` that takes a string and prints the letters in decreasing order of frequency. 

Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http: // en.wikipedia.org/wiki/Letter_frequencies. 

**第 0049 题：More anagrams!

Write a program that reads a word list from a file and prints all the sets of words that are anagrams.

Here is an example of what the output might look like:
```
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']
```
Hint: you might want to build a dictionary that maps from a set of letters to a list of words that can be spelled with those letters. The question is, how can you represent the set of letters in a way that can be used as a key?

1. Modifythepreviousprogramsothatitprintsthelargestsetofanagramsfirst,followedbythe second largest set, and so on.
2. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. What set of 8 letters forms the most possible bingos? Hint: there are seven.

**第 0050 题：**Two words form a “metathesis pair” if you can transform one into the other by swapping two letters; for example, “converse” and “conserve.” Write a program that finds all of the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible swaps. 

**第 0051 题：**Write a function named `choose_from_hist` that takes a histogram as defined and returns a random value from the histogram, chosen with probability in proportion to frequency.

A efficient algorithm is :

1. Use keys to get a list of the words in the book.
2. Build a list that contains the cumulative sum of the word frequencies. The last item in this list is the total number of words in the book, n.
3. Choose a random number from 1 to n. Use a bisection search (Problem 0040 ) to find the index where the random number would be inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list.

Write a program that uses this algorithm to choose a random word from the book. 

**第 0052 题：**Markov analysis:

1. Write a program to read a text from a file and perform Markov analysis. The result should be a dictionary that maps from prefixes to a collection of possible suffixes. The collection might be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your program with prefix length two, but you should write the program in a way that makes it easy to try other lengths.

2. Add a function to the previous program to generate random text based on the Markovan alysis. Here is an example from Emma with prefix length 2

```
He was very clever, be it sweetness or be angry, ashamed or only amused, at such a stroke. She had never thought of Hannah till you were never meant for me?" "I cannot make speeches, Emma:" he soon cut it all himself.
```
For this example, I left the punctuation attached to the words. The result is almost syntactically correct, but not quite. Semantically, it almost makes sense, but not quite.

**第 0053 题：**The “rank” of a word is its position in a list of words sorted by frequency: the most common word has rank 1, the second most common has rank 2, etc.

Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages (http://en.wikipedia.org/wiki/Zipf’s_law ). Specifically, it predicts that the frequency, f, of the word with rank r is:

![](http://ww1.sinaimg.cn/large/8178ba0ejw1ep6j8kt9dwj20l601xt8h.jpg)

where s and c are parameters that depend on the language and the text. If you take the logarithm of both sides of this equation, you get:

![](http://ww2.sinaimg.cn/large/8178ba0ejw1ep6j9cj3v7j20l201ya9v.jpg)

So if you plot log f versus log r, you should get a straight line with slope -s and intercept log c.

Write a program that reads a text from a file, counts word frequencies, and prints one line for each word, in descending order of frequency, with log f and log r. Use the graphing program of your choice to plot the results and check whether they form a straight line. Can you estimate the value of s?

To make the plots, you might have to install matplotlib (see http: // matplotlib. sourceforge. net/ ).

第 0054 题：**Write a function “walks” through a directory, prints the names of all the files, and calls itself recursively on all the directories.

The os module provides a function called walk that is similar to this one but more versatile. Read the documentation and use it to print the names of the files in a given directory and its subdirectories.

**第 0055 题：**Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files, your program should catch the exception, print an error message, and exit.
