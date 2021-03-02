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

  ```python
  # 员工字典(员工编号 部门编号 姓名 工资)
  dict_employees = {
      1001: {"did": 9002, "name": "师父", "money": 60000},
      1002: {"did": 9001, "name": "孙悟空", "money": 50000},
      1003: {"did": 9002, "name": "猪八戒", "money": 20000},
      1004: {"did": 9001, "name": "沙僧", "money": 30000},
      1005: {"did": 9001, "name": "小白龙", "money": 15000},
  }
  # 部门列表
  list_departments = [
      {"did": 9001, "title": "教学部"},
      {"did": 9002, "title": "销售部"},
      {"did": 9003, "title": "品保部"},
  ]
  # 1. 打印所有员工信息,
  # 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
  
  for key,value in dict_employees.items():
      print(f"{value['name']}的员工编号是{key}, 部门编号是{value['did']}, 月薪{value['money']}元")
  
  # 2. 打印所有月薪大于2w的员工信息,
  # 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
  
  for key,value in dict_employees.items():
      if value['money']> 20000:
          print(f"{value['name']}的员工编号是{key}, 部门编号是{value['did']}, 月薪{value['money']}元")
  
  # 3. 在部门列表中查找编号最小的部门
  min_number = list_departments[0]
  
  for i in range(1,len(list_departments)):
      if min_number["did"] > list_departments[i]["did"]:
          min_number = list_departments[i]
  
  print(min_number)
  # 4. 根据部门编号对部门列表序排列
  for r in range(len(list_departments)-1):
      for c in range(r+1,len(list_departments)):
          if list_departments[r]["did"]<list_departments[c]["did"]:
              list_departments[r],list_departments[c] = list_departments[c],list_departments[r]
  
  print(list_departments)
  
  ```

4.参照下列代码,定义函数,计算社保缴纳费用.

```python
 salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))
```

```python
def calculate_fee(salary_before_tax):
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    return  social_insurance

salary_before_tax = float(input("请输入税前工资："))

print(f"个人需要缴纳社保费用：{calculate_fee(salary_before_tax)}"  )

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

```python
def get_min(list_):
    min_value = list_[0]
    for i in range(1, len(list_)):
        if min_value > list_[i]:
            min_value = list_[i]
    return min_value

list01 = [170, 160, 180, 165]
print(get_min(list01))
```

6. 定义函数,根据颜色(RGBA)编号,计算颜色。
   "R" -> "红色"
   "G" -> "绿色"
   "B" -> "蓝色"
   "A" -> "透明度"
   参数:颜色(RGBA)编号
   返回值:颜色

   ```python
   def return_color(rgba_):
       dict_color = {"R": "红色", "G": "绿色", "B": "蓝色", "A": "透明度"}
   		if value in dict_color:
       	return dict_color[rgba_]
   
   rgba_ = input("请输入颜色编号：")
   
   print(return_color(rgba_))
   ```

   