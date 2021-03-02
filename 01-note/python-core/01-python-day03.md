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

    -  <     小于

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
  - 逻辑行：python解释器需要执行的指令。
  -  建议一个逻辑行在一个物理行上。
  - 如果一个物理行中使用多个逻辑行，需要使用分号；隔开。
  - 如果逻辑行过长，可以使用隐式换行或显式换行。
  - 隐式换行：所有括号的内容换行,称为隐式换行。括号包括: () []  {} 三种
  - 显式换行：通过折行符 \ (反斜杠)换行，必须放在一行的末尾，目的是告诉解释器,下一行也是本行的语句。 

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

  -  语法：变量 = 结果1 if 条件 else 结果2

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