## C 练习册

**第 0000 题：**逆序的三位数

程序每次读入一个正三位数，然后输出逆序的数字。注意，当输入的数字含有结尾的0时，输出不应带有前导的0。比如输入700，输出应该是7。

**第 0001 题：**时间换算

UTC是世界协调时，BJT是北京时间，UTC时间相当于BJT减去8。现在，你的程序要读入一个整数，表示BJT的时和分。整数的个位和十位表示分，百位和千位表示小时。如果小时小于10，则没有千位部分；如果小时是0，则没有百位部分；如果分小于10分，需要保留十位上的0。如1124表示11点24分，而905表示9点5分，36表示0点36分，7表示0点7分。

有效的输入范围是0到2359，即你的程序不可能从测试服务器读到0到2359以外的输入数据。

你的程序要输出这个时间对应的UTC时间，输出的格式和输入的相同，即输出一个整数，表示UTC的时和分。整数的个位和十位表示分，百位和千位表示小时。如果小时小于10，则没有千位部分；如果小时是0，则没有百位部分；如果分小于10分，需要保留十位上的0。

提醒：要小心跨日的换算。

**第 0002 题：**信号报告

无线电台的RS制信号报告是由三两个部分组成的：

R(Readability) 信号可辨度即清晰度.

S(Strength)    信号强度即大小.

其中R位于报告第一位，共分5级，用1—5数字表示.

1---Unreadable

2---Barely readable, occasional words distinguishable

3---Readable with considerable difficulty

4---Readable with practically no difficulty

5---Perfectly readable

报告第二位是S，共分九个级别，用1—9中的一位数字表示

1---Faint signals, barely perceptible

2---Very weak signals

3---Weak signals

4---Fair signals

5---Fairly good signals

6---Good signals

7---Moderately strong signals

8---Strong signals

9---Extremely strong signals

现在，你的程序要读入一个信号报告的数字，然后输出对应的含义。如读到59，则输出：

    Extremely strong signals, perfectly readable.

**第 0003 题：**奇偶个数

你的程序要读入一系列正整数数据，输入-1表示输入结束，-1本身不是输入的数据。程序输出读到的数据中的奇数和偶数的个数。


