# Day 01   2020/12/30  星期三

---

## 计算机组成

- 硬件

  - 控制器
  - 运算器  
    （控制器+运算器-->CPU)
  - 存储器

  1. 内存RAM：容量小，速度快，临时存储数据
  2. 硬盘HDD：容量大，速度慢，永久存储数据

    - 输入设备
    - 输出设备

- 软件

  - 操作系统
  - 应用软件：为了某种特定的用途而被开发的软件
  - 软件：程序+文档  
    程序是一组计算机能够识别和执行的指令集合。  
    文档是为了便于了解程序所需的说明性资料。

## python

- 定 义

- 执行方式

  - 交互式 内存中

  - 文件式 保存在硬盘中

    

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

# Day 03   2021/1/4  星期一

---

# 命题

- **bool运算**

  - **bool类型**

    用来表示真和假的类型

    True 表示真(条件满足或成立)，本质是1

    False 表示假(条件不满足或不成立)，本质是0 

    - False的只有0，0.0，None，""(空字符串)

    - 核心：有值则为真

      ```python
      #判断是否有值
      if content:
      	print("输入的是：",content)
      ```

  - **比较类型**

    - <     小于

      <=    小于等于

      \>     大于

      \>=    大于等于

      ==    等于

      !=     不等于

    - 返回布尔类型的值

      比较运算的数学表示方式 : 0 <= x <= 100

- **逻辑运算符**

  - **与 and**

    - 表示并且的关系，一假俱假。    **（尽量把耗时的判断放在后面，提高运行速度）**

      示例:

        True and True   # True

        True and False  # False

        False and True  # False

      False and False  # False

  - **或 or**

    - 表示或者的关系，一真俱真   

      示例:

      True or True    # True

      True or False    # True

      False or True    # True

      False or False   # False 

  - **非 not**

    - 表示取反

      例如：

      not True  # 返回False

      not False # 返回True

      <img src="/Users/chenjingru/chenjr/reference resources/day03/逻辑运算符.jpg" alt="逻辑运算符" style="zoom:50%;" />


  - **优先级**

    高到低：

    算数运算符 + = / * 等

    比较运算符 > < == >=

    增强运算符+= -= 

    身份运算符 is is not

    逻辑运算符 not and or

    a += b/ 3 == c* 2

    相当于先算b/3和 c*2，然后计算 b/ 3 == c* 2，然后a+=0或者a+=1

# 语句

- **行**

  -   物理行：程序员编写代码的行。
  -   逻辑行：python解释器需要执行的指令。
  -   建议一个逻辑行在一个物理行上。
  -   如果一个物理行中使用多个逻辑行，需要使用分号；隔开。
  -   如果逻辑行过长，可以使用隐式换行或显式换行。
  -   隐式换行：所有括号的内容换行,称为隐式换行。括号包括: () []  {} 三种
  -   显式换行：通过折行符 \ (反斜杠)换行，必须放在一行的末尾，目的是告诉解释器,下一行也是本行的语句。 

- **选择语句**

  - if else 语句

    1. 作用:

    ​      让程序根据条件选择性的执行语句，一段代码执行不执行

    2. 语法:

      if 条件1:

    ​    语句块1

      elif 条件2:

    ​    语句块2

      else:

    ​    语句块3

    ```python
    if xxx:
    if xxx:
    if xxx:
    #多路分支，每个if都需要判断，这种写法不好！
    if xxx:
    elif xxx:
    else:
    #当if满足之后，后面的elif不再判断
    #else仅仅归属上面的一个if
    ```

    3. 说明:

      elif 子句可以有0个或多个。

      else 子句可以有0个或1个，且只能放在if语句的最后。 

  - 连续区间的判定只需要写一边

    ```python
    # 练习5：
    # 		根据心理年龄与实际年龄，打印智商等级。
    # 	    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
    #     天才：140以上（包含）
    #     超常：120-139之间（包含）
    #     聪慧：110-119之间（包含）
    #     正常：90-109之间（包含）
    #     迟钝：80-89之间（包含）
    # 低能：80以下
    
    mental_age = int(input("请输入您的心理年龄:"))
    real_age = int(input("请输入您的实际年龄:"))
    
    level = mental_age/real_age *100
    
    if level >=140:
        print("天才")
    elif 120<=level<=139:
        print("超常")
    elif 110<=level<=119:
        print("聪慧")
    elif 90<=level<=109:
        print("正常")
    elif 80<=level<=89:
        print("迟钝")
    else:
        print("低能")
    
    #这样写不好，显示不出连续性，应像下面这样写
    
    if level >= 140:
        print("天才")
    elif level>=120:#执行此句，上面的一定不满足
        print("超常")
    elif level>=110:
        print("聪慧")
    elif level>=90 :
        print("正常")
    elif level>=80:
        print("迟钝")
    else:
        print("低能")
    ```

    ```python
    if month == 1 or  3 or 5 or  7 or  8 or 10 or 12:
        print("31天")
    #输入month=2 输出31天
    #or是判断逻辑命题之间的关系，month==1是一个命题，可真可假，然后和3这个命题去做or
    ```

- if语句的真值表达式

  - if 100:

    ​    print("真值")

    等同于

    if bool(100):

      print("真值")

- 条件表达式

  - 语法：变量 = 结果1 if 条件 else 结果2

    作用：根据条件(True/False) 来决定返回结果1还是结果2。

    ```python
    # 练习：在终端中输入一个整数，如果是奇数为变量state赋值"奇数",否则赋值"偶数"。
    # 效果：
    # 	请输入数字:6
    # state变量存储的是：偶数
    
    num = int(input("请输入一个整数："))
    # state= ""
    # if  num% 2 ==0:
    #     state = "偶数" 
    # else:
    #     state = "奇数"
    # print("state变量存储的是：",state)
    
    state = "奇数" if num % 2 != 0 else "偶数"
    print("state变量存储的是:" + state)
    
    state = "奇数" if num % 2 else "偶数"
    print("state变量存储的是:" + state)     #和2取余有值，num%2！=0
    ```

    ```python
    # 练习：在终端中输入一个年份，如果是闰年为变量day赋值29,否则赋值28。
    #       闰年条件：年份能被4整除但是不能被100整除
    #                 年份能被400整除
    # 效果：
    # 	请输入年份:2020
    # 2020年的2月有29天
    
    while True:
        month = int(input("请输入年份(输入0结束)："))
        if month == 0:
            break
        day = 29 if month % 4 == 0 and month % 100 != 0 or month % 400 == 0 else 28
    
        print(str(month) + "年的2月有" + str(day) + "天")
    ```

- **循环语句**

  - while语句

    作用：程序执行次数的问题

# homework

1. 三（代码demo、图片、理论）合一

2. 当天练习独立完成

3. 写出下列程序运行结果:
   (1)
       input_number = 8
       random_number = 8
       if input_number == random_number:
           print("猜对了")
       else:
           print("猜错了")
   (2)
       num = 12
       if num > 3:
           print("⼤于3")
       elif num > 5:
           print("⼤于5")
       elif num > 10:
           print("⼤于10")
       elif num > 15:
           print("⼤于10")
   (3)
       str_value = ""

       #if str_value:
           #new_str = str_value
       #else:
           #new_str = "empty"
       
       new_str = str_value if str_value else "empty"
       print(new_str)

4. 根据需求写出程序
   (1) 电梯设置规定：
           如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
       步骤:
           终端中获取人数/总重量
           显示电梯正常运行
               电梯超载

   ```python
   # 电梯设置规定：
   #             如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
   #         步骤:
   #             终端中获取人数/总重量
   #             显示电梯正常运行
   #                 电梯超载
   
   num = int(input("请输入人数："))
   weight = float(input("请输入总重量："))
   
   state = "正常运行" if num<=10 and weight <=1000 else "超载"
   
   print(state)
   ```

   (2) 根据年龄，输出对应的人生阶段。
           年龄       ⼈⽣阶段
           0-6 岁      童年
           7-17 岁     少年
           18-40 岁    ⻘年
           41-65 岁    中年
           65 岁之后    ⽼年
       步骤:
           终端中获取年龄
           显示人生阶段

   ```python
   # 根据年龄，输出对应的人生阶段。
   #             年龄       ⼈⽣阶段
   #             0-6 岁      童年
   #             7-17 岁     少年
   #             18-40 岁    ⻘年
   #             41-65 岁    中年
   #             65 岁之后    ⽼年
   #         步骤:
   #             终端中获取年龄
   #             显示人生阶段
   
   age = int(input("请输入您的年龄："))
   if age>65:
       print("老年")
   elif age>40:
       print("中年")
   elif age > 17:
       print("青年")
   elif age>6:
       print("少年")
   elif age>=0:
       print("童年")
   else:
       print("您的输入有误！")
   ```

   (3) 如果是vip客户,消费小于等于500,享受85折
                   消费大于500,享受8折
       如果不是vip客户,消费大于等于800,享受9折
                     消费小于800,原价
       在终端中输入账户类型,消费金额,计算折扣.

   ```python
   # 如果是vip客户,消费小于等于500,享受85折
   #                     消费大于500,享受8折
   #         如果不是vip客户,消费大于等于800,享受9折
   #                       消费小于800,原价
   #         在终端中输入账户类型,消费金额,计算折扣.
   
   
   type = input("请输入账户类型：")
   fee = float(input("请输入消费金额："))
   if type == "vip":
       if fee <= 500:
           discount  = "85折"
       else:
           discount = "8折"
   else:
       if fee>= 800:
           discount = "9折"
       else:
           discount = "没有折扣"
   
   print(discount)
   ```

   (4)
       在终端中录入4个同学体重,打印最轻的值.
       效果：
           请输入第1个同学体重:100
           请输入第2个同学体重:120
           请输入第3个同学体重:93
           请输入第4个同学体重:160
           最轻的同学:93

   ```python
   # 在终端中录入4个同学体重, 打印最轻的值.
   # 效果：
   # 请输入第1个同学体重: 100
   # 请输入第2个同学体重: 120
   # 请输入第3个同学体重: 93
   # 请输入第4个同学体重: 160
   # 最轻的同学: 93
   
   w1 = int(input("请输入第1个同学体重："))
   w2 = int(input("请输入第2个同学体重："))
   w3 = int(input("请输入第3个同学体重："))
   w4 = int(input("请输入第4个同学体重："))
   
   min = w1
   
   if w2 < min:
       min = w2
   if w3 < min:
       min = w3
   if w4 < min:
       min = w4
   
   print("最轻的同学："+ str(min))
   ```

5. 阅读
   程序员的数学第三章

# Day 04   2021/1/5  星期二

---

# 循环语句

## while

- 作用: 

  可以让一段代码满足条件，重复执行。

- 语法:

  - while 条件:

       满足条件执行的语句

    else:

  ​    	不满足条件执行的语句

- 说明:
  -  else子句可以省略。
  - 在循环体内用break终止循环时,else子句不执行。

```python
"""
    循环计数
        三要素
"""
count = 0  # 1. 开始
# count += 1
# count += 1
# count += 1
while count < 3:  # 2. 结束
    print(count)  # 0  1  2
    count += 1  # 3. 间隔
```

```python
"""
    while 条件1:
        循环体
        if 条件2:
            break
    else:
        不满足条件1执行的逻辑
        从条件2退出,不执行当前逻辑

    猜数字2.0
        最多猜3次,如果超过次数,提示"游戏失败"
"""
import random

random_number = random.randint(1,100)
count =0
while count < 3:
    count += 1
    input_number = int(input("请输入数字:"))
    if input_number > random_number:
        print("大了")
    elif input_number<random_number:
        print("小了")
    else:
        print("恭喜猜对啦,总共猜了"+str(count)+"次")
        break
else:
    print("游戏失败")
```

## for 语句

- 作用:

    用来遍历可迭代对象的数据元素。

    可迭代对象是指能依次获取数据元素的对象，例如：容器类型。

-  语法:

    for 变量列表 in 可迭代对象:

    	语句块1

    else:

  ​     语句块2

- 说明:

  -  else子句可以省略。

  - 在循环体内用break终止循环时,else子句不执行。

  

### 内存图

<img src="/Users/chenjingru/chenjr/reference resources/day04/for内存图.jpg" alt="for内存图" style="zoom:50%;" />

```python
"""
    for 循环
"""
message = "我是齐天大圣孙悟空"
for item in message:
    # print(item)
    item = "a"
print(message)  # "我是齐天大圣孙悟空"
```

## range函数

- 作用:

​      用来创建一个生成一系列整数的可迭代对象(也叫整数序列生成器)。

- 语法:

​       range(开始点，结束点，间隔)

- 说明:
  - 函数返回的可迭代对象可以用for取出其中的元素
  - 返回的数字不包含结束点
  - 开始点默认为0
  - 间隔默认值为1

```python
"""
   for - 循环计数
        range 函数:整数生成器
"""
# 写法1:range(开始,结束,间隔)
# 注意:不包含结束值
for item in range(1, 3, 1):
    print(item)
# 写法2:range(开始,结束)
# 注意:间隔默认为1
for item in range(1, 3):
    print(item)
# 写法3:range(结束)
# 注意:开始默认为0
for item in range(3):
    print(item)
```

# 跳转语句

## break语句

- 跳出循环体，后面的代码不再执行。
- 可以让while语句的else部分不执行。

## continue语句

- 跳过本次，继续下次循环。

```python
"""
    累加1--100之间所有整数
    条件:能被3整除
"""
# 思想: 满足条件累加.
sum_value = 0
for item in range(1, 101):
    if item % 3 == 0:
        sum_value += item
print(sum_value)

# 思想: 不满足条件跳过,否则累加.
sum_value = 0  # 1 2 3 ...
for item in range(1, 101):
    if item % 3 != 0:
        continue  # 跳过:继续下次循环
        # break  # 跳出:结束循环
    sum_value += item
print(sum_value)
```

## 小结

- 语句（流程控制语句）

  - 选择语句：能够让程序根据时机场合决定是否执行（让代码根据条件执行）

    ​     if：

    ​			满足条件执行的代码

    ​    else：

    ​			不满足条件执行的代码

  - 循环语句：让代码重复执行

    - while：根据条件让代码重复
      - 例如：纸张对折到珠穆朗玛峰

    - for： 根据次数让代码重复 + range
      - 例如：累加数字

  - 跳转语句：让代码不执行（让后续的代码不执行）

    - break：跳出循环
    - continue：跳出本次循环

# 容器

## 字符串

- 定义：由一系列字符组成的不可变序列容器，存储的是字符的**编码值**。
  - 修改的是变量，字符串每次创建的是新的，没有在原有基础上修改。
  - 因为如果在原有空间修改，可能会破坏其他数据内存空间（损人利己）
  - 如果大内存改到小内存，需要判断，降低了速度，所以是一个牺牲空间换速度的做法
  - 计算机只能存数，存不了文字等。由字变数的过程就是编码，那个数就是编码值。

## 编码

-  字节byte：计算机最小存储单位，等于8 位bit。（一般写为B）-- KB MB GB TB  1024进制

-  字符：单个的数字，文字与符号。

-  字符集(码表)：存储字符与二进制序列的对应关系。

- 编码：将字符转换为对应的二进制序列的过程。

- 解码：将二进制序列转换为对应的字符的过程。

- 编码方式：

  - ASCII编码：包含英文、数字等字符，每个字符1个字节。8位0-255 

    <img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210105152448948.png" alt="image-20210105152448948" style="zoom:75%;" />

    ![image-20210105152513647](/Users/chenjingru/Library/Application Support/typora-user-images/image-20210105152513647.png)

  - GBK编码：兼容ASCII编码，包含21003个中文；英文1个字节，汉字2个字节。（中国国标扩展）

  - Unicode字符集：国际统一编码，旧字符集每个字符2字节，新字符集4字节。

  - UTF-8编码：Unicode的存储与传输方式，英文1字节，中文3字节。（理解为把码表压缩一下）

### 相关函数

- ord(字符串):返回该字符串的Unicode码。
- chr(整数):返回该整数对应的字符串。

```python
"""
    编码
"""
# 文字 --> 数字
number = ord("我")
print(number)  # 25105

# 数字 --> 文字
char = chr(25105)
print(char)  # 我
```

### 字面值

- 单引号内的双引号不算结束符
- 双引号内的单引号不算结束符

#### 三引号作用

- 换行会自动转换为换行符\n
- 三引号内可以包含单引号和双引号
- 作为文档字符串

#### 转义符

- 改变字符的原始含义。\’ \” \””” \n \\ \t \0 空字符 

- 原始字符串：取消转义。

​        **a = r”C:\newfile\test.py”**

### 字符串的格式化

- 定义：

生成一定格式的字符串。

- 语法：

字符串%(变量)

```python
"我的名字是%s,年龄是%s" % (name, age)

print("70秒是%(minute).2d分零%(second)d秒"%{'minute':minute,'second':second})

print("70秒是%.2d分零%d秒"%(minute,second))  #70秒是01分零10秒
```

- 类型码：

%s 字符串   %d整数   %f 浮点数

```python
%.3d  #整数类型占三位  5  --> 005
%.2f  #浮点类型保留小数点后2位，且四舍五入
%5.2f #浮点类型保留小数点后2位，且四舍五入，且总共占位5位，小数点算一位,比如3.14会显示 3.14
```

## 通用操作

### 数学运算符

-  +：用于拼接两个容器
- +=：用原容器与右侧容器拼接,并重新绑定变量
- *：重复生成容器元素*
- =：用原容器生成重复元素, 并重新绑定变量
- < <= > >= == !=：依次比较两个容器中元素,一但不同则返回比较结果。

### 成员运算符

- 语法：

​      数据 in 序列

​      数据 not in 序列

- 作用：

​       如果在指定的序列中找到值，返回bool类型。

```python
"""
    容器通用操作
        数学运算
"""
# 1. 拼接2个容器元素
name = "悟空"
name += "八戒"
print(name)  # 悟空八戒
# 2. 容器元素重复
name = "唐僧"
name *= 2
print(name)  # 唐僧唐僧
# 3. 比较运算：依次比较两个容器中元素,一但不同则返回比较结果。比较的是编码值
print("悟空" > "唐僧")
# 4. 成员运算
# True
print("悟空" in "我是齐天大圣孙悟空")
print("圣孙" in "我是齐天大圣孙悟空")
# False
print("齐圣" in "我是齐天大圣孙悟空")
print("圣大" in "我是齐天大圣孙悟空")
```



# homework

1. 三合一

2. 当天练习独立完成

3. 自学教程的字符串新版占位符f-string
   https://www.runoob.com/python3/python3-string.html

   f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，实例如下：

   ```python
   >>> name = 'Runoob'
   >>> f'Hello {name}'  # 替换变量
   
   >>> f'{1+2}'         # 使用表达式
   '3'
   
   >>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
   >>> f'{w["name"]}: {w["url"]}'
   'Runoob: www.runoob.com'
   ```

   用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。

   在 Python 3.8 的版本中可以使用 **=** 符号来拼接运算表达式与结果：

   ```python
   >>> x = 1
   >>> print(f'{x+1}')   # Python 3.6
   2
   
   >>> x = 1
   >>> print(f'{x+1=}')   # Python 3.8
   'x+1=2'
   ```

   **是否还能保留小数点后多少位？**

   - 结论：
     1. 冒号后直接带数字表示宽度限制，数字前的符号表示填充符，超过限制以e+形式显示
     2. 冒号后数字后带f表示转浮点数，.后面表示保留多少位小数
     3. 注意
        - **保留小数位要带f**  比如保留三位 :.3f
        - 小数点前可以加填充位
        - 直接数字加f，表示补足小数点后的位数至默认精度
        -  使用<>^可以靠左， 靠右，居中显示，另外可以配合填充
        - 时间显示可以使用%Y-%m-%d形式

   ```python
   带f: 0.000
   不带f: 0.0
   带f: 50.085
   不带f: 50.1
   带f: 100.039
   不带f: 1e+02
   带f: 150.076
   不带f: 1.5e+02
   带f: 200.165
   不带f: 2e+02
   带f: 250.269
   不带f: 2.5e+02
   ```

   - f-string大括号外如果需要显示大括号，则应输入连续两个大括号{{ }}；大括号内需要引号，使用引号即可。

     ```python
     f"{{5}}{'apples'}"
     '{5}apples'
     ```

   - **f-string填充**

     -  什么是填充？
       概念：当我们指定了字符串最终的长度的时候，如果现有的字符串没有那么长，那么我们就用某种字符（填充字符）来填满这个长度，这就是“填充”。

     - 默认使用空格填充

       ```python
       >>> name = "Huang Wei"
       >>> f"{name:>20}"
       '           Huang Wei'
       
       >>> f"{name:<20}"
       'Huang Wei           '
       
       >>> f"{name:^20}"
       '     Huang Wei      '
       ```

     - 用指定字符进行填充

       ```python
       >>> name = "Huang Wei"
       >>> f"{name:_>20}"
       '___________Huang Wei'
       
       >>> f"{name:_<20}"
       'Huang Wei___________'
       
       >>> f"{name:_^20}"
       '_____Huang Wei______'
       ```

       **注意：填充分为左填充、右填充、居中填充。左填充表示在字符串左侧填充，右填充表示在字符串右侧填充，居中填充表示在字符串左右两侧对称填充。>表示左填充，<表示右填充，^表示居中填充。记忆方法：括号口朝左边，就表示左填充；括号口朝右边，就表示右填充。**

       

   - 相关格式描述--仅对数值有效

     <img src="https://img-blog.csdnimg.cn/20200201104904911.png" alt="在这里插入图片描述" style="zoom:100%;" />

     ```python
     >>> a = 12
     >>> b = -25
     >>> f"{a:+}"
     '+12'
     >>> f"{b:+}"
     '-25'
     
     >>> f"{a:-}"
     '12'
     >>> f"{b:-}"
     '-25'
     
     >>> f"{a: }"
     ' 12'
     >>> f"{b: }"
     '-25'
     ```

   - 精度

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200201104903588.png)

     ```python
     >>> a = 123.456
     # 只指定width
     >>> f"{a:10}"
     '   123.456'
     # 只指定0width
     >>> f"{a:010}"
     '000123.456'
     # 使用width.precision
     >>> f"{a:8.1f}"
     '   123.5'
     >>> f"{a:8.2f}"
     '  123.46'
     >>> f"{a:.2f}"
     '123.46'
     # 在width后面，直接加f，表示补足小数点后的位数至默认精度6
     >>> f"{a:2f}"
     '123.456000'
     ```

   - 截断

     ```python
     >>> a = "Hello"
     # 当发生截断的时候，如果不指定填充符，默认使用空格填充
     >>> f"{a:10.3}"
     'Hel       '
     # 在发生截断的时候，使用指定的填充符
     >>> f"{a:_>10.3}"
     '_______Hel'
     >>> f"{a:_<10.3}"
     'Hel_______'
     ```

4. 模拟登录
   如果账号的密码错误3次，提示锁定账户，效果如下：
       请输入账号：qtx
       请输入密码：1234
       登录失败
       你还剩余 2 次机会
       请输入账号：Qtx
       请输入密码：1234
       登录失败
       你还剩余 1 次机会
       请输入账号：Qtx
       请输入密码：123456
       登录成功

   ```python
   # 模拟登录
   # 如果账号的密码错误3次，提示锁定账户，效果如下：
   #     请输入账号：qtx
   #     请输入密码：1234
   #     登录失败
   #     你还剩余 2 次机会
   #     请输入账号：Qtx
   #     请输入密码：1234
   #     登录失败
   #     你还剩余 1 次机会
   #     请输入账号：Qtx
   #     请输入密码：123456
   #     登录成功
   
   account_ = "Qtx"
   pwd_ = "123456"
   
   count = 3
   for i in range(count):
       account = input("请输入账号:")
       pwd = input("请输入密码:")
       if account == account_ and pwd == pwd_:
           print("登陆成功")
           break
       else:
           print("登录失败")
           count -= 1
           if count == 0:
               print("你的账户已经锁定")
           else:
               print("你还剩余%d次机会" % count)
               # print(f"你还剩余{count}次机会" )
   
   ```

   ```python
   """
       如果账号的密码错误3次，提示锁定账户，效果如下：
           请输入账号：qtx
           请输入密码：1234
           登录失败
           你还剩余 2 次机会
           请输入账号：Qtx
           请输入密码：1234
           登录失败
           你还剩余 1 次机会
           请输入账号：Qtx
           请输入密码：123456
           登录成功
   """
   
   for count in range(3):  # 0  1   2
       login_id = input("请输入账号：")
       password = input("请输入密码：")
       if login_id == 'Qtx' and password == '123456':
           print("登录成功")
           break
       else:
           print("登录失败")
           # print("你还剩%d次机会" % (2 - count))
           print(f"你还剩{2 - count}次机会")
   else:
       print("登录次数超过3次，你的账号已被锁定")
   ```

   

5. (选做)赌大小游戏
   玩家的身家初始10000，实现下列效果：
       少侠请下注: 30000
       超出了你的身家，请重新投注。
       少侠请下注: 8000
       你摇出了5点,庄家摇出了3点
       恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
       少侠请下注: 18000
       你摇出了6点,庄家摇出了6点
       打平了，少侠，在来一局？
       少侠请下注: 18000
       你摇出了4点,庄家摇出了6点
       少侠,你输了，身家还剩 0
       哈哈哈，少侠你已经破产，无资格进行游戏

   ```python
   # (选做)赌大小游戏
   # 玩家的身家初始10000，实现下列效果：
   #     少侠请下注: 30000
   #     超出了你的身家，请重新投注。
   #     少侠请下注: 8000
   #     你摇出了5点,庄家摇出了3点
   #     恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
   #     少侠请下注: 18000
   #     你摇出了6点,庄家摇出了6点
   #     打平了，少侠，在来一局？
   #     少侠请下注: 18000
   #     你摇出了4点,庄家摇出了6点
   #     少侠,你输了，身家还剩 0
   #     哈哈哈，少侠你已经破产，无资格进行游戏
   
   import random
   
   number_of_coin = 10000
   
   while True:
       num_of_banker = random.randint(1, 7)
       num_of_player = random.randint(1, 7)
   
       out_of_coin = int(input("少侠请下注:"))
   
       if out_of_coin > number_of_coin:
           print("超出了你的身家，请重新投注。")
           continue
       print("你摇出了%d点,庄家摇出了%d点" % (num_of_player, num_of_banker))
       print(f"你摇出了{num_of_player}点,庄家摇出了{num_of_banker}点")
   
       if num_of_banker < num_of_player:
           number_of_coin += out_of_coin
           print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩%d" % number_of_coin)
           print(f"恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩{number_of_coin}")
   
       elif num_of_banker > num_of_player:
           number_of_coin -= out_of_coin
           print("少侠,你输了，身家还剩%d" % number_of_coin)
           print(f"少侠,你输了，身家还剩{number_of_coin}")
           if number_of_coin == 0:
               print("哈哈哈，少侠你已经破产，无资格进行游戏")
               break
   
       else:
           print("打平了，少侠，在来一局？")
   ```

   ```python
   """
   8. (选做)赌大小游戏
       玩家的身家初始10000，实现下列效果：
           少侠请下注: 30000
           超出了你的身家，请重新投注。
           少侠请下注: 8000
           你摇出了5点,庄家摇出了3点
           恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
           少侠请下注: 18000
           你摇出了6点,庄家摇出了6点
           打平了，少侠，在来一局？
           少侠请下注: 18000
           你摇出了4点,庄家摇出了6点
           少侠,你输了，身家还剩 0
           哈哈哈，少侠你已经破产，无资格进行游戏
   """
   import random
   
   money = 10000
   while money > 0:
       bet = int(input("少侠请下注: "))
       if bet > money:
           print("超出了你的身家，请重新投注。")
           continue
       dealer = random.randint(1, 6)
       player = random.randint(1, 6)
       # print("你摇出了" + str(player) + "点,庄家摇出了" + str(dealer) + "点")
       # print("你摇出了%d点,庄家摇出了%d点" % (player, dealer))
       print(f"你摇出了{player}点,庄家摇出了{dealer}点")
       if dealer > player:
           money -= bet
           print("少侠,你输了，身家还剩" + str(money))
       elif dealer < player:
           money += bet
           print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩" + str(money))
       else:
           print("打平了，少侠，在来一局？")
   
   # 可能退出循环，只会因为没钱了.
   print("哈哈哈，少侠你已经破产，无资格进行游戏")
   ```

6. (选做)一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
   提示:
       数据/算法

   ```python
   # (选做)一个小球从100m高度落下,每次弹回原高度一半.
   # 计算:
   #  -- 总共弹起多少次?(最小弹起高度0.01m)
   #  -- 全过程总共移动多少米?
   # 提示:
   #     数据/算法
   
   
   original_height = 100
   count = 0
   distance = original_height
   
   while True:
       original_height /= 2
   
       if original_height < 0.01:
           break
   
       count += 1
       distance += original_height * 2
   
   print("总共弹起%d次(最小弹起高度0.01m)" % count)
   print("全过程总共移动%.2f米" % distance)
   
   print(f"总共弹起{count}次(最小弹起高度0.01m)")
   print(f"全过程总共移动{distance:.2f}米")
   ```

   ```python
   """
   6. 一个小球从100m高度落下,每次弹回原高度一半.
      计算:
       -- 总共弹起多少次?(最小弹起高度0.01m)   13 次
       -- 全过程总共移动多少米?
       数据：高度       次数     距离
       处理：高度/=2   次数+=1  距离+=?
   """
   height = 100
   count = 0
   distance = height
   # 循环条件：下落高度
   # while height  > 0.01:
   # 循环条件：弹起高度
   while height / 2 > 0.01:
       # 弹起来
       height /= 2
       count += 1
       distance += height * 2  # 累加起落
       print(f"第{count}次弹起来的高度是{height}")
   
   # print("总共弹起%d次" % count)
   print(f"总共弹起{count}次")
   # print("全过程总共移动%.2f米" % distance)
   print(f"全过程总共移动{distance:.2f}米")
   ```

   

8.阅读
    https://unicode-table.com/cn/
    程序员的数学第四章：数学归纳法

# Day 05   2021/1/6  星期三

---

# 索引 index

- 作用：定位单个容器元素。

- 语法：容器[整数]

- 说明：
  - 正向索引从0开始，第二个索引为1，最后一个为len(s)-1。
  - 反向索引从-1开始,-1代表最后一个,-2代表倒数第二个,以此类推,第一个是-len(s)。

```Python
"""
    索引
        作用:
            定位单个元素
        语法:
            容器名[整数]
"""
message = "我是花果山齐天大圣"
print(message[2])  # 花
print(message[-2])  # 大
print(len(message)) # 9
# 注意：索引不能越界IndexError
# print(message[99])
# print(message[-99])
```

# 切片 slice

- 作用：

  定位多个容器元素。

- 语法：

  容器[开始索引:结束索引:步长]

- 说明：

  - 结束索引不包含该位置元素

  - 步长是切片每次获取完当前元素后移动的偏移量

  - 开始、结束和步长都可以省略

```python
"""
    切片
        作用:
            定位多个元素
        语法1:
            容器名[开始:结束:间隔]
            注意不包含结束值
        语法2:
            容器名[开始:结束]
            注意间隔默认为1
        语法3:
            容器名[:结束]
            开始默认0
        语法4:
            容器名[:]
            结束默认包含末尾值
"""
# range(开始,结束,间隔)
message = "我是花果山齐天大圣"
print(message[2:5:1])  # 花果山
print(message[2:-4:1])  # 花果山
print(message[2:-4])  # 花果山
print(message[:-4])  # 我是花果山
print(message[:])  # 我是花果山齐天大圣
print(message[-3:])  # 天大圣

message = "我是花果山齐天大圣"
print(message[:2])#我是
print(message[-2:])#大圣
print(message[1: 5])#是花果山
print(message[-2: 3:-1])  # 大天齐山
print(message[1: 1])  # 空
print(message[2: 5:-1])  # 空
# 特殊:翻转
print(message[::-1])  # 圣大天齐山果花是我
```

# 列表

- 字符串：由一系列字符组成的不可变序列容器，存储的是字符的编码值。
- 列表：由一系列变量组成的可变序列容器。（增删改意味着可变）

## 基础操作

- **创建列表：** 

  语法1：列表名 = [元素1,元素2……]  

  ```python
  # 姓名列表
  list_name = ["纪添皓", "沙忠金", "熊志鹏"]
  # 年龄列表
  list_age = [35, 22, 28]
  ```

  语法2：列表名 = list(可迭代对象) -->通过类型转换的方法   可迭代对象：string,range,列表等

  - 一个列表存一个维度的信息，比如都存姓名，都存年龄等

  ```python
  list01 =list("孙悟空") #['孙','悟','空']
  #字符串不可改，但是列表可改，如果想对字符串进行频繁修改，将字符串放入列表中
  ```

- **添加元素：**

  语法1：列表名.append(元素)   

   - 追加——向末尾添加

  ```python
  list_name.append("a")
  ```

  语法2：列表.insert(索引，元素)

   - 插入——在指定位置添加

  ```python
  # -- 插入 陈浩明
  list_name.insert(2, "陈浩明")
  ```

- **定位元素：**

  列表名[索引] = 元素

  变量 = 列表名[索引]

  变量 = 列表名[切片] # 赋值给变量的是切片所创建的新列表(复制/拷贝/备份) 

  - **只有通过切片的才是创建了新列表，索引的没有。**
  - 切片不包含结束

  列表名[切片] = 容器 # 右侧必须是可迭代对象，左侧切片没有创建新列表。

  ```python
  list_name[:2] = ["小纪","小金"]#切片的修改没有创建新的列表，只是遍历右侧可迭代数据，依次存入左侧区域
  ```

  - 支持左右不对等

  ```python
  # 左侧定位0  右侧存入2
  # list_name[1:1] = ["小纪","小金"]
  # 左侧定位2  右侧存入0
  # list_name[:2] = []
  # 报错
  # list_name[:2] = 100
  ```

- **遍历列表：**

     - 正向：

       - 语法一：

          for 变量名 in 列表名:（从头到尾读取）

         ​       变量名就是元素

         ```python
         # 遍历
         # -- 从头到尾读取数据
         for item in list_name:
             print(item)
         ```

       - 语法二：

         for 索引名 in range(len(列表名)):（相当于0——len(列表名)-1）

         ​       列表名[索引名]就是元素

         ```python
         # -- 非从头到尾读取数据
         # for i in range(len(list_name)):
         #     # if 条件:
         #     list_name[i] = "xx"
         ```

         

     - 反向：

          - for 索引名 in range(len(列表名)-1,**-1**,-1):(range不包含结束值)

            ​       列表名[索引名]就是元素

            ```python
            # 开始:总数-1
            # 结束:range不包含-1,实际包含的是0
            # 间隔:倒序
            for i in range(len(list_name)-1,-1,-1):
                print(list_name[i])
            ```

  - **切片和range的区别**
    - range的-1即为-1，0，1，2的-1  range(2,-1,-1)即取的是 2，1，0
    - 切片的-1指的是最后一个元素，[2,-1,-1]如果2是最后一个元素，则取不到任何元素

- **删除元素：**

  语法1：列表名.remove(元素) 

  ```python
  #根据元素移除
  list_name.remove("a") #如果删除的时候不在则报错，异常，所以删除之前要判断一下 if "a" in list_name:
  ```

  语法2：del 列表名[索引或切片]

  ```python
  #根据定位移除  del用来删除变量
  del list_name[-1]
  del list_name[:] #从头到尾删除
  ```

# 深拷贝与浅拷贝（应付面试）

- 拷贝：对数据进行备份，防止错误修改。
- 浅拷贝：（只备份一层）复制过程中，只复制一层变量，不会复制深层变量绑定的对象的复制过程。
  - 优点：占用内存较少
  - 缺点：如果深层数据被修改，互相影响

- 深拷贝：（备份所有层）复制整个依赖的变量。
  - 优点：绝对互不影响
  - 缺点：占用内存过多

- 适用性：
  - 当没有深层数据或者深层数据不会变化的时候，使用浅拷贝。
  - 否则，使用深拷贝。

## 内存图

- 定位的内存图    

  - **关键：列表里存的是变量！**
  - 列表有一份，修改其中之一，互相影响。
  - 列表有两份，修改其中之一，互不影响。（切片会创建和一个新的列表）

  ```python
  list01 = [10,20,30]
  list02 = list01   #赋值  两个变量存一个列表，引用计数变为2 
  data02 = list01[0]  #索引
  data03 = list01[:2]   #切片
  
  #进行修改
  
  data03[0] = 100
  data03[-2:] = [200,300]
  print(list01) #?
  data01[0] = 100
  print(list01) #?
  ```

<img src="/Users/chenjingru/chenjr/reference resources/day05/列表内存图01.jpg" alt="列表内存图01" style="zoom:50%;" />

- 添加和删除的内存图

  ```python
  list01 = [10,20]
  list01.append(30)
  list01.insert(1,40)
  
  list01.remove(20)
  del list01[-1]
  ```

<img src="/Users/chenjingru/chenjr/reference resources/day05/列表内存图03.jpg" alt="列表内存图03" style="zoom:50%;" />

- 深拷贝

  - 修改深拷贝后的数据，互不影响。
  - 修改浅拷贝后的第一层影响，互不影响；修改浅拷贝后的第二层影响，互相影响。

  ```python
  #准备深拷贝工具
  import copy
  list01 = [10,[20,30]]
  list02 = list01[:]
  list03 = copy.deepcopy(list01)
  list02[0] =100
  list02[1][0] = 200
  print(list01)
  
  list03[0] =1000
  list03[1][0] = 2000
  print(list01)
  ```

  ```python
  import copy
  list01 = ["北京",["上海","深圳"]]
  list02 = list01
  list03 = list01[:]
  list04 = copy.deepcopy(list01)
  list04[0] = "北京04"
  list04[1][1] = "深圳04"
  print(list01) # ?['北京', ['上海', '深圳']]
  list03[0] = "北京03"
  list03[1][1] = "深圳03" 
  print(list01) # ?['北京', ['上海', '深圳03']]
  list02[0] = "北京02"
  list02[1][1] = "深圳02"
  print(list02) # ?['北京02', ['上海', '深圳02']]
  ```

<img src="/Users/chenjingru/chenjr/reference resources/day05/深浅拷贝.jpg" style="zoom:50%;" />



<img src="/Users/chenjingru/chenjr/reference resources/day05/深浅拷贝练习.jpg" alt="深浅拷贝练习" style="zoom:50%;" />



# 列表与字符串的转换

- 列表转换为字符串： 

  result = "连接符".join(列表)

  ```python
  """
      1.	列表转换为字符串：
  	result = "连接符".join(列表)
  """
  list01 = ["a", "b", "c"]
  result = "-".join(list01)
  print(result)
  
  # 根据需求拼接字符串
  # 缺点:每次拼接都会产生新字符串,使旧字符串成为垃圾.
  result = ""
  for number in range(10):  # 0 1 2
      # 0
      # 01
      # 012
      result += str(number)
  print(result)
  # 解决:将字符串拼接改为列表追加
  # 思想:将对不可变数据的频繁修改,
  #      改为对可变数据的修改
  result = []
  for number in range(10):
      result.append(str(number))
  result = "".join(result)
  print(result)
  ```

- 字符串转换为列表：

  列表 = “a-b-c-d”.split(“分隔符”)（未讲）

  ```python
  
  ```

# 列表推导式（未讲）

- 定义：

  使用简易方法，将可迭代对象转换为列表。

- 语法：

  变量 = [表达式 for 变量 in 可迭代对象]

  变量 = [表达式 for 变量 in 可迭代对象 if 条件]

  ```python
  
  ```

  

- 说明:

  如果if真值表达式的布尔值为False,则可迭代对象生成的数据将被丢弃。

  

  

   

# homework

1. 三合一(文档/demo/图片)

2. 当天练习独立完成

3. 根据列表中的数字,重复生成*.
   list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
   效果：
     ![image-20210106175428242](/Users/chenjingru/Library/Application Support/typora-user-images/image-20210106175428242.png)

   ```python
   """
       1. 根据列表中的数字,重复生成*.
           list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
       效果：
           *
           **
           ***
           ****
           *****
           ****
           ***
           **
           *
   """
   list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
   # 从头到尾  读取
   for number in list01:
       print("*" * number)
   
   # for i in range(len(list01)):
   #     print("*" * list01[i])
   ```

4. 将列表中的数字累乘
   list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   结果：806400

   ```python
   """
       2. 将列表中的数字累乘
           list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
       结果：806400
   """
   
   list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   result = 1  # 因为1乘以任何数字,都不改变.
   for item in list02:
       result *= item
   print(result)
   ```

5. 将列表中整数的个位不是5和3的数字存入另外一个列表
   list03 = [25, 63, 27, 75, 70, 83, 27]
   结果:[27, 70, 27]

   ```python
   """
       3. 将列表中整数的个位不是5和3的数字存入另外一个列表
           list_numbers = [25, 63, 27, 75, 70, 83, 27]
       结果:[27, 70, 27]
   """
   list_numbers = [25, 63, 27, 75, 70, 83, 27]
   result = []
   for item in list_numbers:
       unit = item % 10
       # if unit == 5 or unit == 3:
       if unit in [5,3]:
           continue
       result.append(item)
   print(result)
   ```

6. 计算列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
   字符串列表：words =["qtx","看一看","想啊想","练练"]
   结果:2

   ```python
   """
       计算给定字符串列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
       字符串列表：words =["qtx","看一看","想啊想","练练"]
   """
   words =["qtx","看一看","想啊想","练练"]
   counter = 0
   for word in words:
       if len(word) > 2 and word[0] == word[-1]:
           counter += 1
   print(counter)
   ```

7. 在终端中录入疫情地区名称，如果输入空字符串，则停止。
   最后倒序打印所有地区名称(一行一个)
   要求：录入的名称已经存在不要再次添加.
   提示： in

   ```python
   """
       在终端中录入疫情地区名称，如果输入空字符串，则停止。
       如果录入的名称已经存在不要再次添加.
       最后倒序打印所有省份名称(一行一个)
   """
   list_regions = []
   while True:
       region = input("请输入疫情地区名称：")
       if region == "":
           break
       if region in list_regions:
           print("已经存在")
       else:
           list_regions.append(region)
   
   for i in range(len(list_regions) - 1, -1, -1):
       print(list_regions[i])
   
   # 通过切片读取数据,会触发浅拷贝,占用内存过多
   # for item in list_regions[::-1]:
   #     print(item)
   ```

8. 在终端中录入5个疫情省份的确诊人数
   最后打印最大值、最小值、平均值.
   （使用内建函数实现）

   ```python
   """
       在终端中录入3个疫情省份的确诊人数
       最后打印最大值、最小值、平均值.（使用内置函数实现）
   """
   list_confirmed_num = []
   for i in range(3):  # 0  1  2
       # confirmed_num = int(input("请输入第%d个确诊人数：" % (i + 1)))
       confirmed_num = int(input(f"请输入第{i + 1}个确诊人数："))
       list_confirmed_num.append(confirmed_num)
   
   print(max(list_confirmed_num))
   print(min(list_confirmed_num))
   print(sum(list_confirmed_num) / len(list_confirmed_num))
   ```

   

# Day 06   2021/1/7  星期四

---

- 字符串转换为列表：

  列表 = “a-b-c-d”.split(“分隔符”)

  ```python
  """
      str --> list
      列表 = "a-b-c-d".split("分隔符")
  """
  list_result = "a-b-c-d".split("-")
  print(list_result)
  # 使用一个字符串存储多个信息
  list_result = "唐僧,孙悟空,八戒".split(",")
  print(list_result)
  ```

```python
"""
    练习：将下列英文语句按照单词进行翻转.
    转换前：To have a government that is of people by people for people
    转换后：people for people by people of is that government a have To
"""
content = "To have a government that is of people by people for people"
list_temp = content.split(" ")
result = " ".join(list_temp[::-1])
print(result)
```

# 列表推导式

- 定义：

  使用简易方法，将可迭代对象转换为列表。

- 语法：

  变量 = [表达式 for 变量 in 可迭代对象]

  变量 = [表达式 for 变量 in 可迭代对象 if 条件]

  ```python
  """
      列表推导式
          列表 = [（对变量的操作 （（for 变量 in 可迭代对象） if 条件））]
  
  """
  list01 = [9, 15, 65, 6, 78, 89]
  # 需求:在list01中挑出能被3整除的数字存入list02
  # list02 = []
  # for item in list01:
  #     if item % 3 == 0:
  #         list02.append(item)
  list02 = [item for item in list01 if item % 3 == 0]
  print(list02)
  # 需求:在list01中所有数字的个位存储list03
  # list03 = []
  # for item in list01:
  #     list03.append(item % 10)
  list03 = [item % 10 for item in list01]
  print(list03)
  ```

  ```python
  """
      练习：
      生成10--30之间能被3或者5整除的数字
      [10, 12, 15, 18, 20, 21, 24, 25, 27]
      生成5 -- 20之间的数字平方
      [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
  """
  # list01 = []
  # for item in range(10,31):
  #     if item % 3 ==0 or item % 5 ==0:
  #         list01.append(item)
  # print(list01)
  list01 = [item for item in range(10, 31) if item % 3 == 0 or item % 5 == 0]
  print(list01)
  
  list02 = [number ** 2 for number in range(5, 21)]
  print(list02)
  ```

  

- 说明:

  如果if真值表达式的布尔值为False,则可迭代对象生成的数据将被丢弃。

  

# 元组

- 定义

  -  由一系列变量组成的**不可变**序列容器。
  - 不可变是指一但创建，不可以再添加/删除/修改元素。  
  - 列表的定义：由一系列变量组成的**可变**序列容器。

- 区别

  - 元组没有预留空间，省地方

  - 元组没有自动扩容，性能高

    <img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210107141024105.png" alt="image-20210107141024105" style="zoom:80%;" />

- 基础操作

  - 创建

    ```python
    """
        元组tuple - 基础操作
            创建
            定位(查找)
            遍历
    """
    # 1. 创建
    # 方式1:
    tuple01 = (10, 20, 30)
    # 方式2:
    list01 = [43, 54, 65, 67]
    tuple02 = tuple(list01)
    print(tuple02)
    # 4. 创建元组时,在没有歧义情况下,括号可以省
    tuple03 = 43, 5, 56, 76
    # 5. 元组只有一个元素时,必须带逗号
    tuple04 = (100,)
    print(type(tuple04))
    ```

  - 定位

    ```python
    # 2. 定位
    print(tuple01[-1])
    print(tuple01[:2])
    ```

  - 遍历

    ```python
    # 3. 遍历
    # 从头到尾读取
    for item in tuple01:
        print(item)
    
    # 非从头到尾读取
    for i in range(len(tuple01) - 1, -1, -1):
        print(tuple01[i])
    
        # 6.序列拆包
    # 语法:  多个变量 = 一个容器
    a, b, c = tuple01
    a, b, c = "孙悟空"
    a, b, c = [100, 200, 300]
    # * 表示接收剩余的数据,结果为列表
    a, *b = tuple01
    print(a)
    print(b)
    print(c)
    ```

```python
# 3月10日
# 31 + 29 + 10
# 练习2：
#     根据月日,计算是这一年的第几天.
#     公式：前几个月总天数 + 当月天数
# 例如：5月10日
#     计算：31  29  31  30 + 10
month = int(input("请输入月份:"))  # 5
day = int(input("请输入天:"))
day_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_days = 0
# for i in range(4):# 0 1 2 3
#     total_days += day_of_month[i]
# total_days = sum(day_of_month[:4])
total_days = sum(day_of_month[:month - 1])
total_days += day
print(total_days)
```

```python
"""
    元组应用
"""

month = int(input("请输入月份:"))
if 1 <= month <= 12:
    if month == 2:
        print("29天")
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in (4, 6, 9, 11):
        print("30天")
    else:
        print("31天")
else:
    print("月份有误")

# 将每月的天数存入元组
day_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(day_of_month[0])
print(day_of_month[2])
```

![image-20210107145431592](/Users/chenjingru/Library/Application Support/typora-user-images/image-20210107145431592.png)

# 字典 dic（一定是无序的，现在python3.5以后有序仅为了方便）

- 定义

  - 由一系列键值对组成的**可变**散列容器。

  - 散列：对键进行哈希运算，确定在内存中的存储位置，每条数据存储无先后顺序。

  - 键必须惟一且不可变(字符串/数字/元组)，值没有限制。

    ![image-20210107145709686](/Users/chenjingru/Library/Application Support/typora-user-images/image-20210107145709686.png)

- 基础操作

  - 创建

    - 字典名 = {键1：值1，键2：值2} 列表竖着存储东西，字典横着存储东西。

      ```python
      # 1. 创建字典
      # 方式1:字典名 = {键1:值1,键2:值2}
      dict_person_gb = {
          "name": "高博",
          "age": 26,
          "sex": "女"
      }
      dict_person_jth = {
          "name": "纪添皓",
          "age": 25,
          "sex": "男"
      }
      ```

    - 字典名 = dict (可迭代对象)  **此可迭代对象的元素必须可以一分为二**（字符串不行，因为字符串是一个整体，不能分割）

      ```python
      # 方式2:字典名 = dict(可迭代对象)
      # 可迭代对象格式要求:元素能够一分二
      list01 = ["唐僧", ("猪", "八戒"), ["沙", "僧"]]
      dict_data = dict(list01)
      print(dict_data)
      ```

  - 添加/修改元素

    - 语法: 

      字典名[键] = 数据

    - 说明:

       键不存在，创建记录。

       键存在，修改值。

      ```python
      dict_person_gb["money"] = 999999
      
      ```

      

  - 获取元素

    - 变量 = 字典名[键]  # 没有键则错误

  - 遍历字典

    - for 键名 in 字典名:

      ​       字典名[键名]

      ```python
      # -- 所有key
      for key in dict_person:
          print(key)
      # -- 所有value
      for value in dict_person.values():
          print(value)
      # -- 所有key value
      # item 得到的是元组 (key,value)
      # for item in dict_person.items():
      #     print(item[0])
      #     print(item[1])
      for k, v in dict_person.items():
          print(k)
          print(v)
      # ['name', 'age', 'sex']
      print(list(dict_person))
      # ['高博', 26, '女']
      print(list(dict_person.values()))
      # [('name', '高博'), ('age', 26), ('sex', '女')]
      print(list(dict_person.items()))
      ```

      

    - for 值名 in 字典名.**values()**:

      ​		 语句

      ```
      
      ```

      

    - for 键名,值名 in 字典名.**items()**:

      ​		语句

      ```
      
      ```

      

  - 删除元素

     - del 字典名[键]

       ```python
       dict_person = {
           "name": "高博",
           "age": 26,
           "sex": "女"
       }
       # 语法：del 字典名[键]
       # del dict_person["sex"]
       # print(dict_person)
       ```

       

- 字典推导式

  - 定义：

    使用简易方法，将可迭代对象转换为字典。

  - 语法:

    {键:值 for 变量 in 可迭代对象}

    {键:值 for 变量 in 可迭代对象 if 条件}

    ```python
    """
        字典推导式
            字典名 = {键:值 for 变量 in 可迭代对象 if 条件}
    """
    # 需求：
    # key:1-10之间的数字
    # value:key的平方
    # dict_result = {}
    # for number in range(1, 11):
    #     dict_result[number] = number ** 2
    dict_result = {number: number ** 2 for number in range(1, 11)}
    print(dict_result)
    
    # 需求：
    # key:1-10之间的奇数
    # value:key的平方
    # dict_result = {}
    # for number in range(1, 11):
    #     if number % 2:
    #         dict_result[number] = number ** 2
    
    dict_result = {
        number: number ** 2
        for number in range(1, 11)
        if number % 2
    }
    print(dict_result)
    ```

# 集合 set

- 定义

  - 由一系列键值对组成的可变散列容器。

  - 由一系列不重复的不可变类型变量(元组/数/字符串)组成的可变散列容器。

  - 相当于只有键没有值的字典(键则是集合的数据)。

    ![image-20210107204035764](/Users/chenjingru/Library/Application Support/typora-user-images/image-20210107204035764.png)

- 基础操作

  - 创建空集合：

    集合名 = set()  

    ```
    
    ```

    集合名 = set(可迭代对象)

    ```
    
    ```

    

  - 创建具有默认值集合：

    集合名 = {1, 2, 3} 

    ```python
    # 1. 创建
    # 方式1
    # 语法：集合名 = {元素1,元素2}
    set01 = {"悟空", "八戒", "唐僧"}
    ```

    集合名 = set(可迭代对象)

    ```python
    # 方式2
    # 语法：集合名 = set(可迭代对象)
    list01 = [5, 4, 5, 56, 5]
    set02 = set(list01)
    ```

  - 添加元素：

    集合名.add(元素)

    ```python
    # 2. 添加
    set01.add("小白龙")
    set01.add("唐僧")
    ```

  - 遍历

    ```python
    for item in set01:
    	print(item)
    ```

  - 删除元素：

    集合名.remove(元素)

    ```python
    # 5. 删除
    set01.remove("小白龙")
    print(set01)
    ```

- 应用

  - 去重复

  - 数学运算

    - 交集&：返回共同元素。

    ```python
    s1 = {1, 2, 3}
    
    s2 = {2, 3, 4}
    
    s3 = s1 & s2 # {2, 3}
    ```

    - 并集：返回不重复元素

    ```python
    s1 = {1, 2, 3}
    
    s2 = {2, 3, 4}
    
    s3 = s1 | s2 # {1, 2, 3, 4}
    ```

    - 补集-：返回只属于其中之一的元素

    ```python
    s1 = {1, 2, 3}
    
    s2 = {2, 3, 4}
    
    s1 - s2 # {1} 属于s1但不属于s2
    ```

    - 补集^：返回不同的的元素

    ```python
    s1 = {1, 2, 3}
    
    s2 = {2, 3, 4}
    
    s3 = s1 ^ s2 # {1, 4}  等同于(s1-s2 | s2-s1)
    ```

    - 子集<：判断一个集合的所有元素是否完全在另一个集合中
    - 超集>：判断一个集合是否具有另一个集合的所有元素

    ```python
    s1 = {1, 2, 3}
    
    s2 = {2, 3}
    
    s2 < s1 # True
    
    s1 > s2 # True
    ```

    - 相同或不同== !=：判断集合中的所有元素是否和另一个集合相同。

    ```python
    s1 = {1, 2, 3}
    
    s2 = {3, 2, 1}
    
    s1 == s2 # True
    
    s1 != s2 # False
    ```

    子集或相同,超集或相同 <= >= 

# homework

1. 三合一

2. 当天练习独立完成

3. 将列表中的数字累减
   list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   提示：初始为第一个元素

   ```python
   # 3. 将列表中的数字累减
   #     list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   #     提示：初始为第一个元素
   
   
   list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   result = list02[0]
   
   for i in range(1,len(list02)):
       result -= list02[i]
   
   
   print(f"结果为:{result}")
   ```

4. 将列表中整数的十位不是3和7和8的数字存入另外一个列表
   list03 = [135, 63, 227, 675, 470, 733, 3127]
   结果:[63, 227, 3127]
   提示：将数字转换为字符串进行处理,通过索引获取十位

   ```python
   # 4. 将列表中整数的十位不是3和7和8的数字存入另外一个列表
   #    list03 = [135, 63, 227, 675, 470, 733, 3127]
   #    结果:[63, 227, 3127]
   #    提示：将数字转换为字符串进行处理,通过索引获取十位
   
   
   list03 = [135, 63, 227, 675, 470, 733, 3127]
   list04 = []
   for item in list03:
       if str(item)[-2] not in ("3","7","8"):
           list04.append(item)
   
   print(f"结果为:{list04}")
   
   
   """
       3. 将列表中整数的十位不是3和7和8的数字存入另外一个列表
           list03 = [135, 63, 227, 675, 470, 733, 3127]
       结果:[63, 227, 3127]
   """
   list03 = [135, 63, 227, 675, 470, 733, 3127]
   result = []
   for item in list03:
       unit = str(item)[-2]
       if unit in ("3", "7", "8"):
           continue
       result.append(item)
   print(result)
   ```

5. 在数字列表中查找最大的数字(不许用内置函数)
   算法：
       [170  ,  160  ,  180  ,  165]
   假设第一个就是最大值
   使用假设的和第二个进行比较, 发现更大的就替换假设的
   使用假设的和第三个进行比较, 发现更大的就替换假设的
   使用假设的和第四个进行比较, 发现更大的就替换假设的
   最后，假设的就是最大的.

   ```python
   # 5. 在数字列表中查找最大的数字(不许用内置函数)
   #     算法：
   #         [170  ,  160  ,  180  ,  165]
   #     假设第一个就是最大值
   #     使用假设的和第二个进行比较, 发现更大的就替换假设的
   #     使用假设的和第三个进行比较, 发现更大的就替换假设的
   #     使用假设的和第四个进行比较, 发现更大的就替换假设的
   #     最后，假设的就是最大的.
   
   list05 = [170, 160, 180, 165]
   
   max_number = list05[0]
   
   for i in range(1,len(list05)):
       if list05[i] > max_number:
           max_number = list05[i]
   
   
   print(f"最大值为：{max_number}")
   ```

   

# Day 07   2021/1/8  星期五

---

# 容器小结

一、种类与特点

字符串：存储字符的编码，不可变，序列（字符串是一种特殊的元组）

列表：存储变量，可变，序列

元组：存储变量，不可变，序列



字典：存储键值对，可变，散列

 - 键的限制：唯一且不变（不可变数据：字符串、元组、数值）

集合：存储健，可变，散列（再看一下什么是散列）

二、可变与不可变

- 面试题1：python有多少种数据类型？
  - 答：只有两种，根据内存存储机制可分为可变与不可变。可变意味着预留空间+自动扩容，例如：列表，字典，集合等；不可变意味着按需分配，例如：字符串，数值，布尔，元组等。
- 面试题2：既然有可变数据为什么还存在不可变数据？
  - 答：不可变数据性能更高，应该优先选择。（存储相同数据内存更少，创建速度更快）

三、序列与散列

- 序列：有顺序，空间连续（节省内存空间），定位灵活（支持索引和切片），定位单个元素较慢。
- 散列：无顺序，数据分布松散（浪费内存空间，利用空间换时间），定位单个元素最快（分门别类找东西才快，因为分好类别了所以无序）。

四、基础操作

- 创建

  ```python
  list01 = [10,20,30]
  dict01 = {"a":"A","b":"B"}
  ```

- 添加

  ```python
  list01.append(40)
  list01.insert(0,50)
  
  dict01["c"] = "C"
  ```

- 定位

  ```python
  print(list[0])
  print(list[-2:])
  
  print(dict01["a"]
  ```

- 遍历

  ```python
  for item in list01:
    print(item)
    
  for i in range(len(list01)-1,-1,-1):#倒序
    print(list01[i])
    
  for key in dict01:
    print(key)
    
  for value in dict01.values():
    print(value)
    
  for key,value in dict01.items():
    print(key)
    print(value)
  ```

- 删除

  ```python
  list01.remove(10)
  del list01[-1]
  
  
  del dict01["a"]
  ```

- 相互转换

  ```python
  #列表变字典(要求：列表中的元素必须可以一分为2)
  print(dict([(1,2),(3,4)]))
  
  
  #字典转成列表
  print(list(dict01))
  print(list(dict01.values()))
  print(list(dict01.items()))
  ```

# 两层循环嵌套

里面要重复多次，外面来个循环

代码重复——>循环

外层循环做一次，内存循环做多次（笛卡尔积）



## 二维列表

- 定位 

  ```python
  """
      二维列表
          列表名[行索引][列索引]
  """
  
  list01 = [
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
  ]
  print(list01[0][0])
  print(list01[1][4])
  ```

# 自定义排序算法

```python
"""
    算法：
        1. 变量交换
            a,b = b,a
        2. 取最值
            list01 = [.....]
            max_value = list01[0]
            for i in range(1,len(list01)):
                if max_value < list01[i]:
                    max_value = list01[i]
        3. 累计运算
            初始值 = ?
            循环 ....
                初始值 += ?
            结果
        4. 自定义排序算法
"""
list01 = [54, 545, 6, 76, 8, 2, 9]
# 升序：小 --> 大
# 降序：大 --> 小
# 思想：
#   容器中所有元素两两比较
# 步骤：
#   在整个范围内,让第一个元素为最小值
# min_value = list01[0]
# for i in range(1, len(list01)):
#     if min_value > list01[i]:
#         min_value = list01[i]
# print(min_value)

# for i in range(1, len(list01)):
#     if list01[0] > list01[i]:
#         list01[0], list01[i] = list01[i], list01[0]
#
# for i in range(2, len(list01)):
#     if list01[1] > list01[i]:
#         list01[1], list01[i] = list01[i], list01[1]

# [取]出数据
for r in range(len(list01) - 1):
    # [比]较最小值
    for c in range(r + 1, len(list01)):
        # 如果发现更小
        if list01[r] > list01[c]:
            # 交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
```



# 函数

- 为了一个功能能够重复使用，之前的都是”做“和”用“混在一起，函数可以使得”做“和”用“相分离，”做“和”变化“绑定

- 如果需要调试时进入函数体，按F7，F8直接跳过函数体

- 参数

  - 本质就是变量
  - 给做功能的人提供的信息

  ```python
  """
      函数
          参数:本质就是变量
             制作功能时要求使用功能时提供的信息
  
  """
  
  
  # 形式参数：表面的不具体的数据
  def attack(count):
      for __ in range(count):
          print("直拳")
          print("摆拳")
          print("勾拳")
  
  
  # 实际参数：真实的具体的数据
  attack(5)
  attack(2)
  ```

- 返回值

  ```python
  """
      返回值
          制作函数时给使用函数时传递的信息
  """
  
  
  # 需求：两个数值相加的函数
  # 缺点：一个函数做了3个功能（输入 计算 输出）
  # def add():
  #     one = int(input("请输入第一个数字："))
  #     two = int(input("请输入第二个数字："))
  #     result = one + two
  #     print("结果是：%d" % result)
  #
  # add()
  
  
  def add(one, two):
      result = one + two
      # 返回 数据
      return result
  
  
  res = add(5, 3)
  print(res)
  ```

  ```python
  """
      返回值语法
  """
  def func01():
      print("func01执行了")
      return 100
  
  # 1. 调用者,可以接收也可以不接收返回值
  func01()
  res = func01()
  print(res)
  
  # 2.在Python语言中,
  # 函数没有return或return后面没有数据,
  # 都相当于return None
  def func02():
      print("func02执行了")
      return
  
  res = func02()
  print(res) # None
  
  # 3.return可以退出函数
  def func03():
      print("func03执行了")
      return
      print("func03又执行了")
  
  func03()
  
  # 4. return 可以退出多层循环嵌套
  def func04():
      while True:
          while True:
              while True:
                  # break 只能退出一层循环
                  print("循环体")
                  return
  
  func04()
  ```

# homework

1. 三合一
2. 当天练习独立完成
3. 容器综合训练(不创建函数)

#员工字典(员工编号 部门编号 姓名 工资)

```python
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}
```

#部门列表

```python
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]
```

- 打印所有员工信息,

  格式：xx的员工编号是xx,部门编号是xx,月薪xx元.

- 打印所有月薪大于2w的员工信息,

  格式：xx的员工编号是xx,部门编号是xx,月薪xx元.

- 在部门列表中查找编号最小的部门

- 根据部门编号对部门列表降序排列

4.参照下列代码,定义函数,计算社保缴纳费用.

```python
 salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))
```

5.定义函数,在列表中获取最小值

```python
 list01 = [170, 160, 180, 165]
    min_value = list01[0]
    for i in range(1, len(list01)):
        if min_value > list01[i]:
            min_value = list01[i]
    print(min_value)
```

6. 定义函数,根据颜色(RGBA)编号,计算颜色。
   "R" -> "红色"
   "G" -> "绿色"
   "B" -> "蓝色"
   "A" -> "透明度"
   参数:颜色(RGBA)编号
   返回值:颜色