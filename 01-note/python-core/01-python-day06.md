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

    