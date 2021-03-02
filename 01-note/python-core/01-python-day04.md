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