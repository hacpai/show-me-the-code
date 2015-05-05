## 数据结构练习册

**第 0000 题：**Maximum Subsequence Sum

Given a sequence of K integers { N1, N2, ..., NK }. A continuous subsequence is defined to be { Ni, Ni+1, ..., Nj } where 1 <= i <= j <= K. The Maximum Subsequence is the continuous subsequence which has the largest sum of its elements. For example, given sequence { -2, 11, -4, 13, -5, -2 }, its maximum subsequence is { 11, -4, 13 } with the largest sum being 20.

Now you are supposed to find the largest sum, together with the first and the last numbers of the maximum subsequence.

**第 0001 题：**一元多项式求导

设计函数求一元多项式的导数。

**输入格式**：以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过1000的整数）。数字间以空格分隔。

**输出格式**: 以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格。注意“零多项式”的指数和系数都是0，但是表示为“0 0”。

**第 0002 题：**可变数组的实现

**第 0003 题：**线程安全的链表的实现

**第 0004 题：**图

1. Download thinkcomplex. com/ GraphCode. py , which contains the code in this chapter. Run it as a script and make sure the test code in main does what you expect.

2. Make a copy of GraphCode.py called Graph.py. Add the following methods to Graph, adding test code as you go.

3. Write a method named get_edge that takes two vertices and returns the edge between them if it exists and None otherwise. Hint: use a try statement.

4. Write a method named remove_edge that takes an edge and removes all references to it from the graph.

5. Write a method named vertices that returns a list of the vertices in a graph.

6. Write a method named edges that returns a list of edges in a graph. Note that in our representation of an undirected graph there are two references to each edge.

7. Write a method named out_vertices that takes a Vertex and returns a list of the adjacent vertices (the ones connected to the given node by an edge).

8. Write a method named out_edges that takes a Vertex and returns a list of edges connected to the given Vertex.

9. Write a method named add_all_edges that starts with an edgeless Graph and makes a complete graph by adding edges between all pairs of vertices.

![](http://i.imgur.com/fcMg0z1.png)
