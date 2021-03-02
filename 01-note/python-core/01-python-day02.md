# Day 02   2020/12/31  星期四

---

# pycharm快捷键

- 到行首：command+<-   /fn+ <-
- 到行尾：command+->   /fn+ -> 
- 注释：command+/
- 复制一行：command+D
- 删除一行：command+Y
- 选择行：
- 选择列：potion+⇧+鼠标点击
- 格式化：option+command+L
- 选中向右 ⇥ 右制表符（Tab键）  
- 选中向左 ⇧ Shift  +⇥ 右制表符（Tab键）
- 更改变量名 ⇧+F6
- 自动填入参数、自动导入 ⌥ Option+回车
- main 快捷键
- Command + P        参数信息（在方法中调用参数）
- Ctrl + J       快速查看文档
- Ctrl + Alt + M  提取方法（好像不对）
- shift+command+L 改名

## Mac键盘符号和修饰键说明
- ⌘ Command  
- ⇧ Shift  
- ⌥ Option（Alt）
- ⌃ Control  
- ↩︎ Return/Enter  
- ⌫ Delete  
- ⌦ 向前删除键（Fn+Delete）  
- ↑ 上箭头  
- ↓ 下箭头  
- ← 左箭头  
- → 右箭头  
- ⇞ Page Up（Fn+↑）  
- ⇟ Page Down（Fn+↓）  
- Home Fn + ←  
- End Fn + →  
- ⇥ 右制表符（Tab键）  
- ⇤ 左制表符（Shift+Tab）  
- ⎋ Escape (Esc)

# 数据基本运算

# input, print

<img src="/Users/chenjingru/Downloads/day02/人机交互.jpg" alt="人机交互" style="zoom:50%;" />

- **demo01**

  ```python
  """
      练习:创建文件exercise01.py抄写下列代码
      汇率转换器
  """
  # 1. 获取数据
  usd = float(input("请输入美元:"))
  # 2. 逻辑计算
  cny = usd * 6.5208
  # 3. 显示结果
  print(str(usd) + "美元=" + str(cny) + "人民币")
  ```

- **demo02**

  ```python
  """
      函数
          print
  """
  # 1. 字面意思:打印
  # 2. 作用:将括号中的内容显示在终端中
  # 3. 语法:print(内容)
  # 4. 适用性:显示结果
  print("你好")
  print("世界")
  ```

- **demo03**

  ```python
  """
      函数
          input
  """
  # 1. 字面意思:输入
  # 2. 作用:将终端中输入的内容存储在程序中
  # 3. 语法:结果 = input(提示信息)
  # 4. 适用性:获取数据
  name = input("请输入姓名:")
  age = input("请输入年龄:")
  print(name + "的年龄是:" + age + ".")
  ```

  

# char(非课上，记录一下)

1.	ord(字符串):返回该字符串的Unicode码。
2.	chr(整数):返回该整数对应的字符串。

# 变量
程序运行在哪里？--内存  
程序处理什么？--按照代码在处理数据  
作用：在内存中操作数据  
= 是赋值的意思，将右边的结果赋值一份给左侧

- **demo04**

  ```python
  """
      变量
          问题:
              程序运行在哪里? -- 内存
              程序在处理什么? -- 数据
          作用:
              在内存中操作数据
          语法:
              变量名 = 数据
          赋值号:
              将右侧结果复制一份给左侧
  """
  # 创建变量
  name01 = "孙悟空"
  name02 = "唐僧"
  name03 = name01 + name02
  # 修改变量
  name01 = "悟空"
  # 变量赋值变量
  name04 = name01
  print(name03)
  ```

- **demo05**

  ```python
  """
      删除变量
          del
  """
  name01 = "悟空"
  name02 = name01
  del name01
  print(name02)
  
  a1 = "唐僧"
  ```

## 内存图

数据或变量赋值时总是传递数据地址

- 创建变量

  <img src="/Users/chenjingru/Downloads/day02/变量内存图1.jpg" alt="变量内存图1" style="zoom:50%;" />

- 修改变量

- 删除变量 del

  <img src="/Users/chenjingru/Downloads/day02/del内存图.jpg" alt="del内存图" style="zoom:50%;" />

- 建议命名：字母小写，多个单词下划线隔开

# 核心数据类型  
在python中变量没有类型，但关联的对象有类型。
- 整型 int
- 浮点型 float
- 字符串 str
	- type(变量)：返回变量的类型  
	
	- 从终端当中获取的数据都是str，如果需要str都需要类型转换  
	
	- 转换成int都是向下取整数  
	
	  **demo06** 
	
	  ```python
	  """
	      数据类型
	  """
	  # 1. 字符串str:存储文字
	  name = "悟空"
	  # 字符拼接
	  str_number = "1234" + "5"
	  print(str_number)  # 12345
	  
	  # 2. 整形int:存储整数
	  # 数学运算
	  number01 = 1234 + 5
	  print(number01)  # 1239
	  
	  # 3. 浮点型float:存储小数
	  number02 = 123.4
	  ```
	
	  **demo07**
	
	  ```python
	  """
	      类型转换
	          适用性:
	              从终端中获得的数据类型都是str
	              如果需要数学计算,必须类型转换
	          语法:
	              结果 = 目标类型(待转数据)
	  
	  """
	  #　结果 = 目标类型(待转数据)
	  # age = int(input("请输入年龄:"))
	  # print("明年:"+str(age + 1))
	  
	  # str -> int
	  data01 = int("3")
	  # int -> str
	  data02 = str(5)
	  
	  # str -> float
	  data03 = float("1.2")
	  # float -> str
	  data04 = str(1.2)
	  
	  # int -> float
	  data05 = float(250)
	  # float -> int
	  data06 = int(1.9)
	  print(data06)  # 向下取整(截断删除)
	  
	  # 注意：字符串转换为其他类型时,
	  # 必须是目标类型的字符串表达形式
	  # print(int("10.5"))　# 报错
	  # print(float("abc"))# 报错
	  ```
- 结果 = 目标类型（待转数据）
	- 字符串转换成其他类型时，必须是目标类型的字符串表达形式 
	
	  ```python
	  print(int(10.5))   #报错
	  ```

# 算术运算符

- /  除法（得到的是小数）

- // 地板除（向下取整）

- % 取余（余数）

- ** 幂运算（乘方）

  <img src="/Users/chenjingru/Downloads/day02/算术运算符.jpg" alt="算术运算符" style="zoom:50%;" />

- **demo08**

  ```python
  """
      运算符
          算数运算符
              + - *  整数商//  小数商/  余数%  幂运算**
  
  """
  data01 = 5
  data02 = 2
  data03 = data01 + data02
  print(data03)
  
  print(data01 % data02) # 1
  print(data01 // data02) # 2
  print(data01 / data02) # 2.5
  print(data01 ** data02) # 5*5
  ```

  

## 优先级

优先级从高到低：

​			 ()

​            **

​         \*  / % //

​         \+ -

## 增强运算符

y += x     相当于 y = y + x

y -= x      相当于 y = y - x

y *= x      相当于 y = y * x

y /= x      相当于 y = y / x

y //= x     相当于 y = y // x

y %= x     相当于 y = y % x

y =** x         相当于 y = y ** x

- **demo09**

  ```python
  """
      运算符
          增强运算符
              在算数运算符基础上,对自身赋值
              +=  -= *=  /=  //=  %=  **=
  """
  data01 = 10
  # 相加产生新数据,但不影响旧数据
  # data01 + 5
  # data01 = data01 + 5
  data01 += 5 # 累加
  print(data01)  # 15
  ```

> ```
> # 练习：在终端中输入一个四位整数，计算每位相加和。
> # 例如：录入1234，打印1+2+3+4结果
> # 效果：
> # 请输入四位整数：1234
> # 结果是：10
> ```

```python
number = 1234
unit01 = number %10
#1234//10 ->123%10 = 3
unit02 = number//10%10
unit03 = number//100%10
unit04 =number//1000
sum = unit01+unit02+unit03+unit04
#这种写法不好，扩展性不强。
number = 1234
sum1 = number %10
#1234//10 ->123%10 = 3
sum1 += number//10%10
sum1 += number//100%10
sum1 +=number//1000
#写成增强的写法，能够扩展
```

<img src="/Users/chenjingru/Downloads/day02/增强运算符.jpg" alt="增强运算符" style="zoom:50%;" />

# homework

1. 三合一(文档/代码demo/图片)

2. 当天练习独立完成(exercise.py)

3. 画出下列代码内存图,说出终端显示结果
   - ​    data01 = 100
     ​    data02 = 200
     ​    data03 = data01 + data02
     ​    data01 = 200
     ​    print(data03) # ?
     
     <img src="/Users/chenjingru/chenjr/reference resources/day03/内存图练习01.jpg" alt="内存图练习01" style="zoom:50%;" />
     
     
     
   - ​    bridegroom_name = "武大郎"
     ​    bride_name = "潘金莲"
     ​    temp = bridegroom_name
     ​    bridegroom_name = bride_name
     ​    bride_name = temp
     ​    print("交换后的新郎：" + bridegroom_name)  # ?
     ​    print("交换后的新娘：" + bride_name)  # ?
     
     <img src="/Users/chenjingru/chenjr/reference resources/day03/变量交换.jpg" alt="变量交换" style="zoom:50%;" />
   
4. 根据父母身高,预测儿子身高.
   步骤:获取父亲身高
       获取母亲身高
       显示儿子身高
   公式:(父亲身高+母亲身高)*0.54
   
   ```python
   # 根据父母身高,预测儿子身高.
   #     步骤:获取父亲身高
   #         获取母亲身高
   #         显示儿子身高
   #     公式:(父亲身高+母亲身高)*0.54
   father_height = float(input("请输入父亲的身高："))
   mother_height = float(input("请输入母亲的身高："))
   
   print((father_height+mother_height)*0.54)
   ```
   
5. 温度转换器：
   摄氏度 = （华氏度 - 32） 除以 1.8
   在终端中录入摄氏度，计算华氏度

   ```python
   # 温度转换器：
   #     摄氏度 = （华氏度 - 32） 除以 1.8
   #     在终端中录入摄氏度，计算华氏度
   
   
   centigrade = float(input("请输入摄氏度："))
   print("华氏度为：", centigrade * 1.8 + 32)
   ```

6. 根据工资计算个人社保缴纳费用
   步骤：在终端中录入工资,根据公式计算,显示缴纳费用
   公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%

   ```python
   # 根据工资计算个人社保缴纳费用
   #     步骤：在终端中录入工资,根据公式计算,显示缴纳费用
   #     公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%
   
   
   salary = float(input("请输入您的工资："))
   
   fee = salary * (0.08 +0.02+0.002+0.12) +3
   
   print("一共缴纳：",fee,"元")
   ```

7. 阅读
   链接：https://pan.baidu.com/s/1JYK5A91CvBg36IhRphiyrg
   提取码：qitx
   程序员的数学第一章
   Python编程：从入门到实践 第一章