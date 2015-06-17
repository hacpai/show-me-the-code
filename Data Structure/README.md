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

**第 0005 题：**随机图

Create a file named RandomGraph.py and define a class named RandomGraph that inherits from Graph and provides a method named add_random_edges that takes a probability p as a parameter and, starting with an edgeless graph, adds edges at random so that the probability is p that there is an edge between any two nodes.

**第 0006 题：**字符串循环右移

*题目内容：*

输入一个字符串和一个非负整数N，要求将字符串循环右移N次。

*输入格式：*

输入在第1行中给出一个字符串，以'#'表示结束，‘＃’不是字符串的一部分，字符串的长度未知，但至少有一个字符；输入的第2行给出非负整数N。

*输出格式：*

在一行中输出循环右移N次后的字符串。

*输入样例：*

    Hello World!#
    2
*输出样例：*

    d!Hello Worl

**第 0007 题：**最小包围矩形

*题目内容：*

给定一组二维坐标，表示直角坐标系内的一个多边形的连续的顶点的坐标序列。计算能包围这个多边形的平行于坐标轴的最小矩形，输出它的左下角和右上角的坐标。

*输入格式:*

第一行是一个正整数n表示顶点的数量，第二行是n组整数，依次表示每个顶点坐标的x和y值。

*输出格式：*

四个整数，依次表示所计算的矩形的左下角的坐标的x、y值和右上角坐标的x、y值。

*输入样例：*
    5
    1 1 1 4 3 7 4 4 4 1

*输出样例：*
    1 1 4 7

**第 0008 题：**分数比较

*题目内容：*

本题要求编写程序，比较两个分数的大小。

*输入格式:*

输入在一行中按照“a1/b1 a2/b2”的格式给出两个分数形式的有理数，其中分子和分母全是int类型范围内的正整数。

*输出格式：*

在一行中按照“a1/b1 关系符 a2/b2”的格式输出两个有理数的关系。其中“>”表示“大于”，“<”表示“小于”，“=”表示“等于”。
注意在关系符前后各有一个空格。

*输入样例：*
    1/2 3/4

*输出样例：*
    1/2 < 3/4

**第 0009 题：**队列的实现

定义的接口
```
Queue init_queue();
void enqueue(Queue *q, Elemtype e);
void print_queue(Queue *q);
Node *get_head(Queue *q);
Node *dequeue(Queue *q);
void clear_queue(Queue *q);
void destory_queue(Queue *q);
```

**第 0010 题：**堆栈的实现

定义的接口
```
Stack init_stack();
void push_stack(Stack *s, Elemtype e);
void print_stack(Stack *s);
int stack_length(Stack *s);
int is_stack_empty(Stack *s);
int is_stack_full(Stack *s);
Elemtype get_top_stack(Stack *s);
Elemtype pop_stack(Stack *s);
void clear_stack(Stack *s);
void free_stack(Stack *s);
```

**第 0011 题：**二叉排序树的实现

定义的接口
```
BiTree init_bitree();
void insert_bi_sort_tree(BiTree *pTree, char *s);
BiTNode *create_bi_sort_tree(BiTree *pTree, char *s);
void access(BiTNode *pNode);
void preorder_traverse(BiTNode *pNode);
void midorder_traverse(BiTNode *pNode);
void postorder_traverse(BiTNode *pNode);
void preorder_traverse_not_recur(BiTNode *pNode);
void midorder_traverse_not_recur(BiTNode *pNode);
void postorder_traverse_not_recur(BiTNode *pNode);
BiTNode *find_bitnode(BiTree *pTree, ElementType e);
BiTNode *find_last_bitnode(BiTree *pTree, ElementType e);
BiTNode *find_left_bitree_largest_bitnode(BiTNode *pNode);
BiTNode *find_right_bitree_littlest_bitnode(BiTNode *pNode);
BiTNode *delete_leaf_bitnode(BiTree *pTree, BiTNode *current, BiTNode *last);
BiTNode *delete_degree_is_one_bitnode(BiTree *pTree, BiTNode *current, BiTNode *last);
BiTNode *delete_degree_is_two_bitnodes(BiTree *pTree, BiTNode *current, BiTNode *last);
BiTNode *delete_bitnode(BiTree *pTree, ElementType e);
```

**第 0012 题：**十进制转换N进制

定义的接口
    char *decimal_to_base_n(int decimal_num, int n);

**第 0013 题：**图的实现

定义的接口

```
Graph* init_vertex(Graph *g);
int find_element(vertex vex[], int n, vertex x);
Graph* init_edge(Graph *g);
Graph init_graph();
void display_graph(Graph *g);
void access(vertex vex);
```

**第 0014 题：**非递归实现前序，中序，后序遍历二叉树

**第 0015 题：**二叉平衡树(AVL 树)的实现

定义的接口

```
AvlTree *init();
int height(AvlTree *t);
int max(int a, int b);
AvlTree *insert(AvlTree *t, ElementType x);
AvlTree *single_rotate_with_left(AvlTree *t);
AvlTree *single_rotate_with_right(AvlTree *t);
AvlTree *double_rotate_left_right(AvlTree *t);
AvlTree *double_rotate_right_left(AvlTree *t);
```

**第 0016 题：**图的深度优先搜索算法和广度优先搜索算法
