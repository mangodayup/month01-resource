# 自学笔记

---

# 列表 https://www.runoob.com/python3/python3-list.html

- 列表都可以进行的操作包括索引，切片，加，乘，检查成员。

- 此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。

- 列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。

- 列表的数据项不需要具有相同的类型。

- 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

  ```python
  list1 = ['Google', 'Runoob', 1997, 2000]
  list2 = [1, 2, 3, 4, 5 ]
  list3 = ["a", "b", "c", "d"]
  list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
  ```

## 访问列表中的值

- 与字符串的索引一样，列表索引从 **0** 开始，第二个索引是 **1**，依此类推。通过索引列表可以进行截取、组合等操作。

  <img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210112155310434.png" alt="image-20210112155310434" style="zoom:50%;" />

- 索引也可以从尾部开始，最后一个元素的索引为 **-1**，往前一位为 **-2**，以此类推。

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210112155335369.png" alt="image-20210112155335369" style="zoom:50%;" />

- 使用下标索引来访问列表中的值，同样也可以使用方括号 **[]** 的形式截取字符，（切片）如下所示：**（不包含结束值）**

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210112155411990.png" alt="image-20210112155411990" style="zoom:50%;" />

## 更新列表

- 可以对列表的数据项进行直接修改或更新

  ```python
  list = ['Google', 'Runoob', 1997, 2000]
   
  print ("第三个元素为 : ", list[2])
  list[2] = 2001
  print ("更新后的第三个元素为 : ", list[2])
  
  #输出结果
  #第三个元素为 :  1997
  #更新后的第三个元素为 :  2001
  ```

- append()方法

## 删除列表元素

- del方法

  ```python
  list = ['Google', 'Runoob', 1997, 2000]
   
  print ("原始列表 : ", list)
  del list[2]
  print ("删除第三个元素 : ", list)
  #输出结果
  #原始列表 :  ['Google', 'Runoob', 1997, 2000]
  #删除第三个元素 :  ['Google', 'Runoob', 2000]
  ```

- remove方法

## Python列表函数&方法

#### 函数

- len(list)方法：返回列表元素个数。

  ```python
  list1 = ['Google', 'Runoob', 'Taobao']
  print (len(list1))
  list2=list(range(5)) # 创建一个 0-4 的列表
  print (len(list2))
  
  #输出结果
  #3
  #5
  ```

- max(list)方法：返回列表元素中的最大值。

  ```python
  list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
  
  print ("list1 最大元素值 : ", max(list1))
  print ("list2 最大元素值 : ", max(list2))
  
  #输出结果
  #list1 最大元素值 :  Taobao
  #list2 最大元素值 :  700
  ```

- min(list)方法：返回列表元素中的最小值。

  ```python
  list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
  
  print ("list1 最小元素值 : ", min(list1))
  print ("list2 最小元素值 : ", min(list2))
  
  #输出结果
  #list1 最小元素值 :  Google
  #list2 最小元素值 :  200
  ```

- list(seq)方法：用于将元组或字符串转换为列表。

  ```python
  aTuple = (123, 'Google', 'Runoob', 'Taobao')
  list1 = list(aTuple)
  print ("列表元素 : ", list1)
  
  str="Hello World"
  list2=list(str)
  print ("列表元素 : ", list2)
  
  #输出结果
  #列表元素 :  [123, 'Google', 'Runoob', 'Taobao']
  #列表元素 :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
  ```

#### 方法

- [list.append(obj)](https://www.runoob.com/python3/python3-att-list-append.html)
  在列表末尾添加新的对象

  ```python
  list1 = ['Google', 'Runoob', 'Taobao']
  list1.append('Baidu')
  print ("更新后的列表 : ", list1)
  
  #输出结果
  #更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']
  ```

- [list.count(obj)](https://www.runoob.com/python3/python3-att-list-count.html)
  统计某个元素在列表中出现的次数

  ```python
  aList = [123, 'Google', 'Runoob', 'Taobao', 123];
  
  print ("123 元素个数 : ", aList.count(123))
  print ("Runoob 元素个数 : ", aList.count('Runoob'))
  
  #输出结果
  #123 元素个数 :  2
  #Runoob 元素个数 :  1
  ```

- [list.extend(seq)](https://www.runoob.com/python3/python3-att-list-extend.html)
  在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

  ```python
  list1 = ['Google', 'Runoob', 'Taobao']
  list2=list(range(5)) # 创建 0-4 的列表
  list1.extend(list2)  # 扩展列表
  print ("扩展后的列表：", list1)
  
  #输出结果
  #扩展后的列表： ['Google', 'Runoob', 'Taobao', 0, 1, 2, 3, 4]
  
  #不同数据类型
  # 语言列表
  language = ['French', 'English', 'German']
   
  # 元组
  language_tuple = ('Spanish', 'Portuguese')
   
  # 集合
  language_set = {'Chinese', 'Japanese'}
   
  # 添加元组元素到列表末尾
  language.extend(language_tuple)
   
  print('新列表: ', language)
   
  # 添加集合元素到列表末尾
  language.extend(language_set)
   
  print('新列表: ', language)
  #输出结果
  #新列表:  ['French', 'English', 'German', 'Spanish', 'Portuguese']
  #新列表:  ['French', 'English', 'German', 'Spanish', 'Portuguese', 'Japanese', 'Chinese']
  ```

- [list.index(obj)](https://www.runoob.com/python3/python3-att-list-index.html)
  从列表中找出某个值第一个匹配项的索引位置，如果没有找到对象则抛出异常。

  ```python
  #list.index(x[, start[, end]])
  #x-- 查找的对象。
  #start-- 可选，查找的起始位置。
  #end-- 可选，查找的结束位置。
  
  list1 = ['Google', 'Runoob', 'Taobao']
  print ('Runoob 索引值为', list1.index('Runoob'))
  print ('Taobao 索引值为', list1.index('Taobao'))
  
  #Runoob 索引值为 1
  #Taobao 索引值为 2
  
  list1 = ['Google', 'Runoob', 'Taobao', 'Facebook', 'QQ']
  # 从指定位置开始搜索
  print ('Runoob 索引值为', list1.index('Runoob',1))
  #Runoob 索引值为 1
  ```

  

- [list.insert(index, obj)](https://www.runoob.com/python3/python3-att-list-insert.html)
  将对象插入列表，插入在索引为index的位置

  ```python
  list1 = ['Google', 'Runoob', 'Taobao']
  list1.insert(1, 'Baidu')#将Baidu插入在索引为1的位置
  print ('列表插入元素后为 : ', list1)
  
  #输出结果
  #列表插入元素后为 :  ['Google', 'Baidu', 'Runoob', 'Taobao']
  ```

- [list.pop(\[index=-1\])](https://www.runoob.com/python3/python3-att-list-pop.html)
  移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

  ```python
  #list.pop([index=-1])
  #index 可选参数：要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
  list1 = ['Google', 'Runoob', 'Taobao']
  list1.pop()
  print ("列表现在为 : ", list1)
  list1.pop(1)
  print ("列表现在为 : ", list1)
  #输出结果
  #列表现在为 :  ['Google', 'Runoob']
  #列表现在为 :  ['Google']
  ```

- [list.remove(obj)](https://www.runoob.com/python3/python3-att-list-remove.html)
  移除列表中某个值的第一个匹配项

  ```python
  list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
  list1.remove('Taobao')
  print ("列表现在为 : ", list1)
  list1.remove('Baidu')
  print ("列表现在为 : ", list1)
  
  #输出结果
  #列表现在为 :  ['Google', 'Runoob', 'Baidu']
  #列表现在为 :  ['Google', 'Runoob']
  ```

- [list.reverse()](https://www.runoob.com/python3/python3-att-list-reverse.html)
  反向列表中元素

  ```python
  list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
  list1.reverse()
  print ("列表反转后: ", list1)
  
  #输出结果
  #列表反转后:  ['Baidu', 'Taobao', 'Runoob', 'Google']
  ```

- [list.sort( key=None, reverse=False)](https://www.runoob.com/python3/python3-att-list-sort.html)
  对原列表进行排序

  ```python
  #list.sort( key=None, reverse=False)
  #key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
  #reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
  
  aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
   
  aList.sort()
  print ( "List : ", aList)
  
  ##输出结果
  #List :  ['Facebook', 'Google', 'Runoob', 'Taobao']
  
  # 列表
  vowels = ['e', 'a', 'u', 'o', 'i']
   
  # 降序
  vowels.sort(reverse=True)
   
  # 输出结果
  print ( '降序输出:', vowels )
  
  #输出结果
  #降序输出: ['u', 'o', 'i', 'e', 'a']
  
  
  #以下实例演示了通过指定列表中的元素排序来输出列表：
  # 获取列表的第二个元素
  def takeSecond(elem):
      return elem[1]
   
  # 列表
  random = [(2, 2), (3, 4), (4, 1), (1, 3)]
   
  # 指定第二个元素排序
  random.sort(key=takeSecond)
   
  # 输出类别
  print ('排序列表：', random)
  
  #输出结果
  #排序列表：[(4, 1), (2, 2), (1, 3), (3, 4)]
  ```

- [list.clear()](https://www.runoob.com/python3/python3-att-list-clear.html)
  清空列表

  ```python
  list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
  list1.clear()
  print ("列表清空后 : ", list1)
  
  #输出结果
  #列表清空后 :  []
  ```

- [list.copy()](https://www.runoob.com/python3/python3-att-list-copy.html)
  复制列表

  ```python
  list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
  list2 = list1.copy()
  print ("list2 列表: ", list2)
  
  #输出结果
  #list2 列表:  ['Google', 'Runoob', 'Taobao', 'Baidu']
  
  
  list1 = [[1,2,3],[2,3,4],[3,4,5]]
  list2 = list1.copy()
  print ("list2 列表: ", list2)
  
  list1[0][0] =2
  print ("list2 列表: ", list2)
  
  #输出结果
  #list2 列表:  [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
  #list2 列表:  [[2, 2, 3], [2, 3, 4], [3, 4, 5]]
  
  #copy()函数是浅拷贝，改变第一层不会有影响，但是改变嵌套的内容会发生影响
  ```

  

# 字符串https://www.runoob.com/python3/python3-string.html

- 字符串是 Python 中最常用的数据类型。我们可以使用引号( **'** 或 **"** )来创建字符串。

- 创建字符串很简单，只要为变量分配一个值即可。例如：

  ```python
  var1 = 'Hello World!'
  var2 = "Runoob"
  ```

## 访问字符串中的值

- Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

- Python 访问子字符串，可以使用方括号 **[]** 来截取字符串，字符串的截取的语法格式如下：
  - 变量[头下标:尾下标]

- 索引值以 **0** 为开始值，**-1** 为从末尾的开始位置。

  <img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210112172240541.png" alt="image-20210112172240541" style="zoom:50%;" />

## 字符串更新

```python
var1 = 'Hello World!'
 
print ("已更新字符串 : ", var1[:6] + 'Runoob!')

#输出结果
#已更新字符串 :  Hello Runoob!
```

## 转义字符

| 转义字符    | 描述                                                         | 实例                                                         |
| :---------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| \(在行尾时) | 续行符                                                       | `>>> print("line1 \ ... line2 \ ... line3") line1 line2 line3 >>> ` |
| \\\         | 反斜杠符号                                                   | `>>> print("\\") \`                                          |
| \\\'        | 单引号                                                       | `>>> print('\'') '`                                          |
| \\\"        | 双引号                                                       | `>>> print("\"") "`                                          |
| \a          | 响铃                                                         | `>>> print("\a")`执行后电脑有响声。                          |
| \b          | 退格(Backspace)                                              | `>>> print("Hello \b World!") Hello World!`                  |
| \000        | 空                                                           | `>>> print("\000") >>> `                                     |
| \n          | 换行                                                         | `>>> print("\n")  >>>`                                       |
| \v          | 纵向制表符                                                   | `>>> print("Hello \v World!") Hello        World! >>>`       |
| \t          | 横向制表符                                                   | `>>> print("Hello \t World!") Hello    World! >>>`           |
| \r          | 回车，将 **\r** 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 **\r** 后面的内容完全替换完成。 | `>>> print("Hello\rWorld!") World! >>> print('google runoob taobao\r123456') 123456 runoob taobao` |
| \f          | 换页                                                         | `>>> print("Hello \f World!") Hello        World! >>> `      |
| \yyy        | 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。           | `>>> print("\110\145\154\154\157\40\127\157\162\154\144\41") Hello World!` |
| \xyy        | 十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行    | `>>> print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21") Hello World!` |
| \other      | 其它的字符以普通格式输出                                     |                                                              |

------

## 字符串运算符

下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：

| 操作符 | 描述                                                         | 实例                            |
| :----- | :----------------------------------------------------------- | :------------------------------ |
| +      | 字符串连接                                                   | a + b 输出结果： HelloPython    |
| *      | 重复输出字符串                                               | a*2 输出结果：HelloHello        |
| []     | 通过索引获取字符串中字符                                     | a[1] 输出结果 **e**             |
| [ : ]  | 截取字符串中的一部分，遵循**左闭右开**原则，str[0:2] 是不包含第 3 个字符的。 | a[1:4] 输出结果 **ell**         |
| in     | 成员运算符 - 如果字符串中包含给定的字符返回 True             | **'H' in a** 输出结果 True      |
| not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True           | **'M' not in a** 输出结果 True  |
| r/R    | 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 **r**（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 | `print( r'\n' ) print( R'\n' )` |
| %      | 格式字符串                                                   | 请看下一节内容。                |

## 格式化字符串

| 符  号 | 描述                                 |
| :----- | :----------------------------------- |
| %c     | 格式化字符及其ASCII码                |
| %s     | 格式化字符串                         |
| %d     | 格式化整数                           |
| %u     | 格式化无符号整型                     |
| %o     | 格式化无符号八进制数                 |
| %x     | 格式化无符号十六进制数               |
| %X     | 格式化无符号十六进制数（大写）       |
| %f     | 格式化浮点数字，可指定小数点后的精度 |
| %e     | 用科学计数法格式化浮点数             |
| %E     | 作用同%e，用科学计数法格式化浮点数   |
| %g     | %f和%e的简写                         |
| %G     | %f 和 %E 的简写                      |
| %p     | 用十六进制数格式化变量的地址         |

format函数



## f-string

## 内建函数



# 字典

# 集合

