# Day 09   2021/1/12  星期二

---

# 函数参数

## 小结

- 实际参数：与形参相对应

  - 位置实参：按顺序

    - 函数名（数据1，数据2）

    - 序列参数：
      - 函数名（*序列）

  - 关键字实参：按名字

    - 函数名（形参名1 = 数据1，形参名2 =数据2……）
    - 字典实参：拆
      - 函数名（**字典）

- 形式参数：
  - 默认形参：实参可选
    - def 函数名（形参名1 = 数据1，形参名2 =数据2……）
  - 位置形参：实参必填
    - def 函数名（形参名1，形参名2）
  - 星号元组形参：多个位置实参合为一个元组
    - def 函数名（*args）
  - 双星号字典形参：多个关键字实参合成一个字典
    - def 函数名（**kargs）
  - 命名关键字形参：必须是关键字实参
    - def函数名（*args，形参名）
    - def函数名（*，形参名）
  - 命名位置实参(第十种新增的)



**顺序：位置形参 --> 星号元组形参 --> 命名关键字形参 --> 双星号字典形参**

```python
def func01(list_target):
    print(list_target)# ?
def func02(*args):# 三合一 实际接收到的是一个元组
    print(args)# ?
def func03(*args,**kwargs):# 三合一 无限，可以为空，但是不能混着来,关键字实参必须在位置实参之后
    print(args)# ?
    print(kwargs)# ?
def func04(p1,p2,*,p4,**kwargs):
    print(p1)# 10
    print(p2)# 20
    print(p4)# 30
    print(kwargs)# {p5 : 40}

func01([1,2,3])#[1,2,3]
func02(*[1,2,3])# 一拆三 实际传递的是三个整数 （1 2 3）
func03(1,2,3,a=4,b=5,c=6) #（1,2,3）  {'a': 4, 'b': 5, 'c': 6}
func04(10,20,p4 = 30,p5 = 40)#10 20 30 {p5 : 40}
```

# 面向对象 Object Oriented

## 概述

### 面向过程

1. 分析出解决问题的步骤，然后逐步实现。

   例如：婚礼筹办

- 发请柬（选照片、措词、制作）
- 宴席（场地、找厨师、准备桌椅餐具、计划菜品、购买食材）
- 婚礼仪式（定婚礼仪式流程、请主持人）

2. 公式：程序 = 算法 + 数据结构

3. 优点：所有环节、细节自己掌控。

4. 缺点：考虑所有细节，工作量大。 

### 面向对象（用人类的思维方式来解决软件的问题）

1. 找出解决问题的人，然后分配职责。	

   例如：婚礼筹办

- 发请柬：找摄影公司（拍照片、制作请柬）
-  宴席：找酒店（告诉对方标准、数量、挑选菜品） 
- 婚礼仪式：找婚庆公司（对方提供司仪、制定流程、提供设备、帮助执行）

2. 公式：程序 = 对象 + 交互

3. 优点

1）思想层面：

- 可模拟现实情景，更接近于人类思维。
- 有利于梳理归纳、分析解决问题。

2）技术层面：

- 高复用：对重复的代码进行封装，提高开发效率。
- 高扩展：增加新的功能，不修改以前的代码。
- 高维护：代码可读性好，逻辑清晰，结构规整。

4. 缺点：学习曲线陡峭。

```python
"""现实世界         编程世界
客观事物 -抽象化->类-具体化->对象
"""
```



## 基础概念

- 抽象：从具体事物中抽离出共性、本质，舍弃个别、非本质过程。

- 类：一个抽象的概念，即生活中的“类别”。

- 对象：类的具体实例，即归属于某个类别的“个体”。

- 类是创建对象的“模板”。

  - 数据成员：名词类型的状态。

  - 方法成员：动词类型的行为。

- 类与类行为不同，对象与对象数据不同。

- 基本公式

  ```
  
  ```

  

## 语法

### 定义类

1. 代码

   ```python
   class 类名: 
     
   	def __init__(self,参数列表):
   
      		self.实例变量 = 参数
   
       	方法成员 
   ```

2. 说明

- 类名所有单词首字母大写.
- ____init____ 也叫构造函数，创建对象时被调用，也可以省略。

- self 变量绑定的是被创建的对象，名称可以随意。
- 生成参数快捷键：option+回车

### 创建对象（实例化）

- 变量 = 类名(参数列表)

  ```python
  class Wife:
      def __init__(self,name,face_score,money):
          self.name = name
          self.face_score = face_score
          self.money = money
  
      def play(self):
           print(self.name,"在玩耍")
  
  jian_ning = Wife("建宁",95,9999999)
  jian_ning.money += 1
  jian_ning.play() 
  ```

- 内存图

  <img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210112162633734.png" alt="image-20210112162633734" style="zoom:50%;" />

# homework

1. 三合一

2. 当天练习独立完成

3. 创建桌子类
        数据：品牌,材质,尺寸(长,宽,高)
   创建电脑类
        数据:型号,CPU型号,内存大小,硬盘大小
        行为：开机,关机

   ```python
   """
       现实世界             编程世界
               -抽象->      类      -具体->      对象
                         class 老婆    老婆(建宁,26,93)
                             姓名
                          年龄
                             颜值
   
       创建桌子类
           数据：品牌,材质,尺寸(长,宽,高)
       创建电脑类
           数据:型号,CPU型号,内存大小,硬盘大小
           行为：开机,关机
   """

   
   # 现实事物  -抽象-> 类　-具体-> 对象
   class Desk:
       def __init__(self, brand="", material="", size=()):
           self.brand = brand
           self.material = material
           self.size = size
   
   
   class Computer:
       def __init__(self, model_number="", cpu="", memory=0, hard_disk=()):
           self.model_number = model_number
           self.cpu = cpu
           self.memory = memory
           self.hard_disk = hard_disk
   
       def starting_up(self):
           print(self.model_number, "开机")
   
       def shutdown(self):
           print(self.model_number, "关机")
   
   
   lege = Desk("乐歌", "复合板材", (112, 29.5, 16))
   print(lege.size)
   
   alienware = Computer("外星人ALW17M", "Intel i7", 16, (256, 1024))
   # starting_up(alienware)
   alienware.starting_up()
   alienware.shutdown()
   ```
   
   
   
4. 创建员工类/部门类,修改实现下列功能.

    1. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    2. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    3. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
    4. 定义函数,查找薪资最少的员工
    5. 定义函数,根据薪资对员工列表升序排列

   ```python
   # 员工列表
       list_employees = [
           {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
           {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
           {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
           {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
           {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
       ]
   
       # 部门列表
       list_departments = [
           {"did": 9001, "title": "教学部"},
           {"did": 9002, "title": "销售部"},
       ]
   
   ```

   ```python
   class Employee:
       def __init__(self, eid, did, name, money):
           self.eid = eid
           self.did = did
           self.name = name
           self.money = money
   
   
   class Department:
       def __init__(self, did, title):
           self.did = did
           self.title = title
   
   
   # 员工列表
   list_employees = [
       Employee(1001, 9002, "师父", 60000),
       Employee(1002, 9001, "孙悟空", 50000),
       Employee(1003, 9002, "猪八戒", 20000),
       Employee(1004, 9001, "沙僧", 30000),
       Employee(1005, 9001, "小白龙", 15000),
   ]
   # 部门列表
   list_departments = [
       Department(9001, "教学部"),
       Department(9002, "销售部")
   ]
   
   
   # 1. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
   def print_employee_info(emp):
       print(f"{emp.name}的员工编号是{emp.eid},部门编号是{emp.did},月薪{emp.money}元.")
   
   
   def print_employee_infos():
       for emp in list_employees:
           print_employee_info(emp)
   
   
   # 2. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
   def print_employees_gt_2w():
       for emp in list_employees:
           if emp.money > 20000:
               print_employee_info(emp)
   
   
   # 3. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
   def print_employees_for_department():
       # 取员工
       for emp in list_employees:
           # 找部门
           for dep in list_departments:
               if emp.did == dep.did:
                   print(f"{emp.name}的部门是{dep.title},月薪{emp.money}元.")
                   break #找到就退出本层循环！！！！！
   
   
   # 4. 查找薪资最少的员工
   def employee_min_by_money():
       min_value = list_employees[0]
       for i in range(1, len(list_employees)):
           if min_value.money > list_employees[i].money:
               min_value = list_employees[i]
       return min_value
   
   
   # 5. 根据薪资对员工列表降序排列
   def ascending_employee_by_money():
       for r in range(len(list_employees) - 1):
           for c in range(r + 1, len(list_employees)):
               if list_employees[r].money < list_employees[c].money:
                   list_employees[r], list_employees[c] = list_employees[c], list_employees[r]
   
   
   # 如果直接打印自定义对象,默认是内存地址
   # 希望查看实例变量,可以通过自定义对象的__dict__
   min_value = employee_min_by_money()
   print(min_value.__dict__)
   ```

   