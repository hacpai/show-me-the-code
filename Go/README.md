## Go 练习册

**第 0000 题：**创建二维 slice

实现 `Pic`。它返回一个 slice 的长度 `dy`，和 slice 中每个元素的长度的 8 位无符号整数 `dx`。当执行这个程序，它会将整数转换为灰度（好吧，蓝度）图片进行展示。

图片的实现已经完成。可能用到的函数包括 `(x+y)/2` 、 `x*y` 和 `x^y`（使用 math.Pow 计算最后的函数）。

（需要使用循环来分配 `[][]uint8` 中的每个 `[]uint8`。）

（使用 uint8(intValue) 在类型之间进行转换。）

**第 0001 题：**用 map 记录词频

实现 `WordCount`。它应当返回一个含有 s 中每个 “词” 个数的 map。函数 wc.Test 针对这个函数执行一个测试用例，并输出成功还是失败。

你会发现 strings.Fields 很有帮助。

**第 0002 题：**斐波纳契闭包

实现一个 fibonacci 函数，返回一个函数（一个闭包）可以返回连续的斐波纳契数。

**第 0003 题：**type Stringer interface { String() string } 接口

让 IPAddr 类型实现 fmt.Stringer 以便用点分格式输出地址。

例如，`IPAddr{127,0,0,1}` 应当输出 `"127.0.0.1"`。

**第 0004 题：**用牛顿法实现开方函数。

牛顿法是通过选择一个初始点 z 然后重复这一过程求 Sqrt(x) 的近似值：

    z = z - (z^2-x) / (2*z)

为了做到这个，只需要重复计算 10 次，并且观察不同的值（1，2，3，……）是如何逐步逼近结果的。 然后，修改循环条件，使得当值停止改变（或改变非常小）的时候退出循环。观察迭代次数是否变化。结果与 [math.Sqrt](http://golang.org/pkg/math/#Sqrt) 接近吗？

提示：定义并初始化一个浮点值，向其提供一个浮点语法或使用转换：

z := float64(1)
z := 1.0

**第 0005 题：** error 接口

从之前的练习中复制 Sqrt 函数，并修改使其返回 error 值。

Sqrt 接收到一个负数时，应当返回一个非 nil 的错误值。复数同样也不被支持。

创建一个新类型

    type ErrNegativeSqrt float64

为其实现

    func (e ErrNegativeSqrt) Error() string

使其成为一个 `error`， 该方法就可以让 ErrNegativeSqrt(-2).Error() 返回 `"cannot Sqrt negative number: -2"`。

注意： 在 Error 方法内调用 fmt.Sprint(e) 将会让程序陷入死循环。可以通过先转换 e 来避免这个问题：`fmt.Sprint(float64(e))`。请思考这是为什么呢？

修改 Sqrt 函数，使其接受一个负数时，返回 ErrNegativeSqrt 值。

**第 0006 题：** Reader

实现一个 Reader 类型，它不断生成 ASCII 字符 'A' 的流。

**第 0007 题：**rot13Reader

一个常见模式是 io.Reader 包裹另一个 `io.Reader`，然后通过某种形式修改数据流。

例如，gzip.NewReader 函数接受 `io.Reader`（压缩的数据流）并且返回同样实现了 io.Reader 的 `*gzip.Reader`（解压缩后的数据流）。

编写一个实现了 io.Reader 的 `rot13Reader`， 并从一个 io.Reader 读取， 利用 rot13 代换密码对数据流进行修改。

已经帮你构造了 rot13Reader 类型。 通过实现 Read 方法使其匹配 `io.Reader`。

**第 0008 题：** HTTP 处理

实现下面的类型，并在其上定义 ServeHTTP 方法。在 web 服务器中注册它们来处理指定的路径。

type String string

type Struct struct {
    Greeting string
    Punct    string
    Who      string
}
例如，可以使用如下方式注册处理方法：

http.Handle("/", Hello{})
http.Handle("/string", String("I'm a frayed knot."))
http.Handle("/struct", &Struct{"Hello", ":", "Gophers!"})
