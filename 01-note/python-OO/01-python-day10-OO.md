# Day 10   2021/1/13  星期三

---

# 复习

```python
"""
    函数参数
        实际参数:与形参进行对应
            位置实参:按顺序
                    函数名(数据1,数据2)
                序列实参:拆
                    函数名(*序列)
            关键字实参:按名称
                    函数名(形参名1 = 数据1,形参名2 = 数据2)
                字典实参:拆
                    函数名(**字典)
        形式参数:限制实参
            默认形参:可选
                    def 函数名(形参名1 = 数据1,形参名2 = 数据2)
            位置形参:必填
                    def 函数名(形参名1,形参名2)
            不定长参数
                星号元组形参:合
                    def 函数名(*args)
                双星号字典形参:合
                    def 函数名(**kwargs)
            命名关键字形参:必须使用关键字实参
                def 函数名(*args,形参名)
                def 函数名(*,形参名)
    面向对象
        目的:了解软件架构
        流程: 现实世界        编程世界
             客观事物 -抽象-> 类 -具体-> 对象
        类:
            class 类名:
                def __init__(self,参数):
                    self.实例变量 = 参数
                    self.方法名称()

                def 方法名称(self):
                    方法体
                    self.数据
        对象:
            对象名 = 类名(具体数据)
            对象名.方法名称()
        实例变量核心价值：
            表达不同对象的不同数据
"""
```

# 类变量和实例变量

## 实例成员

### 实例变量

1. 语法

- 定义：对象.变量名

- 调用：对象.变量名 

  不建议通过类名访问实例变量(虽然可以，但是不建议，不要这么做)

2. 说明

(1) 首次通过对象赋值为创建，再次赋值为修改.

w01 = Wife()

w01.name = "丽丽"

w01.name = "莉莉"

(2) 通常在构造函数(__init__)中创建。

w01 = Wife("丽丽",24)

print(w01.name)

(3) 每个对象存储一份，通过对象地址访问。 

3. 作用：描述某个对象的数据。

4. \_\_dict__：对象的属性，用于存储自身实例变量的字典。

### 实例方法

1. 语法

- 定义：  def 方法名称(self, 参数列表):

​                             方法体

- 调用： 对象地址.实例方法名(参数列表)

​                    不建议通过类名访问实例方法(虽然可以，但是不建议，不要这么做)

2. 说明

- 至少有一个形参，第一个参数绑定调用这个方法的对象,一般命名为"self"。

- 无论创建多少对象，方法只有一份，并且被所有对象共享。

3. 作用：表示对象行为。

## 类成员

### 类成员

1. 语法

-  定义：在类中，方法外定义变量。

​        class 类名:

​             变量名 = 表达式

- 调用：类名.变量名

​        不建议通过对象访问类变量(虽然可以，但是不建议，不要这么做)

2. 说明

- 存储在类中。

- 只有一份，被所有对象共享。

3. 作用：描述所有对象的共有数据。

### 类方法

1. 语法

- 定义：

​      @classmethod

​      def 方法名称(cls,参数列表):

​             方法体

- 调用：类名.方法名(参数列表) 

  ​       不建议通过对象访问类方法(虽然可以，但是不建议，不要这么做)

2. 说明

- 至少有一个形参，第一个形参用于绑定类，一般命名为'cls'

- 使用@classmethod修饰的目的是调用类方法时可以隐式传递类。（python是自动传递对象，加了@classmethod修饰才是自动传递类）

- 类方法中不能访问实例成员，实例方法中可以访问类成员。

3. 作用：操作类变量。

## 内存图

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210113111853581.png" alt="image-20210113111853581" style="zoom:50%;" />

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210113111827873.png" alt="image-20210113111827873" style="zoom:50%;" />

## 例子

```python
"""
    类成员
"""


class ICBC:
    # 类变量:不同对象相同数据  ［大家的］
    total_money = 1000000

    def __init__(self, name="", money=0):
        # 实例变量:不同对象不同数据　　［自己的］
        self.name = name
        self.money = money
        # 创建支行时,总行的钱减少了
        ICBC.total_money -= money


tian_tian = ICBC("天坛支行", 100000)
print(ICBC.total_money)

xi_dan = ICBC("西单支行", 200000)
print(ICBC.total_money)

# 天坛支行钱变动，不影响西单支行
tian_tian.money += 10000
print(xi_dan.money)
```

```python
"""
    小结-Python语言变量
"""
# 全局变量:整个文件可用
data01 = 10

def func01():
    # 局部变量:一个函数可用
    data02 = 20

class MyClass:
    # 类变量:通过类名调用
    data04 = 40
    def __init__(self):
        # 实例变量:通过对象调用
        self.data03 = 30

m01 = MyClass()
print(m01.data03)
print(MyClass.data04)
```

# 三大特征

## 封装

### 数据角度讲

- 定义：

  将一些基本数据类型复合成一个自定义类型。

- 优势：

  - 将数据与对数据的操作相关联。
  - 代码可读性更高（类是对象的模板）。

### 行为角度讲

1. 定义：

   向类外提供必要的功能，隐藏实现的细节。

2. 优势：

   简化编程，使用者不必了解具体的实现细节，只需要调用对外提供的功能。

3. 私有成员：

- 作用：无需向类外提供的成员，可以通过私有化进行屏蔽。

- 做法：命名使用双下划线开头。

- 本质：障眼法，实际也可以访问。

  私有成员的名称被修改为：

  \_(单下划线)类名\_\_(双下划线)成员名，可以通过\_dict_属性或dir函数查看。

4. 属性@property：

将方法的使用方式像操作变量一样方便，从而保护实例变量。（保障数据在有效范围内）

- 定义：

  @property

  def 属性名(self):

   	 return self.__属性名

  @属性名.setter

  def 属性名(self, value):

  ​	  self.__属性名= value

- 调用：

  对象.属性名 = 数据

  变量 = 对象.属性名

- 说明：

  通常两个公开的属性，保护一个私有的变量。

   @property 负责读取，@属性名.setter 负责写入

   只写：属性名= property(None, 写入方法名)

```

```

- 属性的多种写法

  - 读写属性：干预/控制对数据的读写过程   
    - 快捷键：props + 回车
    - 有写入属性就不要直接给私有变量赋值
  - 只读属性：干预/控制对数据的读过程，拒绝写入
    - 快捷键：prop + 回车
    - 适用性：类中自行确定的数据，对外只希望读取，不希望修改

  - 只写属性：干预/控制对数据的写入过程，拒绝读取（访问）

### 设计角度讲

1. 定义：

- 分而治之

  将一个大的需求分解为许多类，每个类处理一个独立的功能。 

- 变则疏之

  变化的地方独立封装，避免影响其他类。

- 高内 聚

  类中各个方法都在完成一项任务(单一职责的类)。 

- 低耦 合 

  类与类的关联性与依赖度要低(每个类独立)，让一个类的改变，尽少影响其他类。

2. 优势：

   便于分工，便于复用，可扩展性强。

# homework

1. 三合一

2. 当天练习独立完成

3. 画出下列代码内存图
   找出打印结果

```python
1. g01 = 100
      g02 = 100
      g03 = [100]
   
   def func01():
       g01 = 200
       g03[0] = 200
   
   def func02():
       global g02
       g02 = 200
   
   func01()
   print(g01)  # ?
   print(g03) #  ?
   func02()
   print(g02)  # ?
   ```
   
   ```python
   class MyClass:
       cls01 = 300
       def __init__(self):
       self.ins01 = 400
   
       self.ins01 += 1
       MyClass.cls01 += 1
   instance01 = MyClass()
   print(instance01.ins01) # ?
   print(MyClass.cls01)   # ?
   
   instance02 = MyClass()
   print(instance02.ins01) # ?
   print(MyClass.cls01)  # ?
   ```

```python
"""
    画出下列代码内存图
    找出打印结果
"""
g01 = 100
g02 = 100
g03 = [100]

def func01():
    g01 = 200# 创建一个局部变量
    g03[0] = 200 # 修改的是列表中元素(读取全局变量)

def func02():
    global g02
    g02 = 200

func01()
print(g01)  # 100
print(g03) #  200
func02()
print(g02)  # 200


class MyClass:
    cls01 = 300 # 饮水机

    def __init__(self):
        self.ins01 = 400 # 杯子

        self.ins01 += 1
        MyClass.cls01 += 1

instance01 = MyClass()# 400->401  300 -> 301
print(instance01.ins01)  # 401
print(MyClass.cls01)  # 301

instance02 = MyClass()# 400->401  301 -> 302
print(instance02.ins01)  # 401
print(MyClass.cls01)  # 302
```

1. 创建电脑类,保护数据在有效范围内
   数据:型号,   CPU型号,    内存大小,    硬盘大小
            不超过10个字符    大于0    元组长度大于等于1

   ```python
   """
       5. 创建电脑类,保护数据在有效范围内
           数据:型号,   CPU型号,    内存大小,    硬盘大小
                   不超过10个字符    大于0    元组长度大于等于1
   """
   
   
   class Computer:
       def __init__(self, model_number="", cpu="", memory=0, hard_disk=()):
           self.model_number = model_number
           self.cpu = cpu
           self.memory = memory
           self.hard_disk = hard_disk
   
       @property
       def cpu(self):
           return self.__cpu
   
       @cpu.setter
       def cpu(self, value):
           if len(value) <= 10:
               self.__cpu = value
           else:
               raise Exception("cpu星号过长")
   
       @property
       def memory(self):
           return self.__memory
   
       @memory.setter
       def memory(self, value):
           if value > 0:
               self.__memory = value
           else:
               raise Exception("cpu星号过长")
   
       @property
       def hard_disk(self):
           return self.__hard_disk
   
       @hard_disk.setter
       def hard_disk(self, value):
           if len(value) >= 1:
               self.__hard_disk = value
           else:
               raise Exception("硬盘数量必须大于等于1")
   
   
   alienware = Computer("外星人ALW17M", "Intel i7", 16, (256, 1024))
   print(alienware.model_number)
   alienware.cpu = "xxx"# cpu("xxx")
   print(alienware.cpu)
   print(alienware.memory)
   print(alienware.hard_disk)
   ```

   

2. (选做)2048核心算法
    list_merge = [2,0,0,2]

    (1)定义零元素向后移动函数(操作全局变量)
    [2,0,0,2] --> [2,2,0,0]
    [2,0,2,0] --> [2,2,0,0]

    (2)定义合并数据函数(操作全局变量)
        调用上面函数
        相邻相同则合并
        [2,2,0,0] --> [4,0,0,0]
        [4,0,2,2] --> [4,2,2,0] --> [4,4,0,0]
        [2,2,2,2] --> [4,4,0,0]
        ...

```python
"""
    2048 游戏核心算法
"""

list_merge = [2,2,0,2]
# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
# 测试
# zero_to_end()
# print(list_merge)

# zero_to_end()
# print(list_merge)


# 2. 定义合并函数(向左移动的核心算法)　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    # [2,2,4,4]
    for i in range(len(list_merge) - 1):  # 取前三个  i
        if list_merge[i] == list_merge[i + 1]:  # 与下一个比 i + 1
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]  # 删除下一个(因为不是当前,所以不存在漏删)
            list_merge.append(0)  # 因为删除一个,补充一个,所以不存在越界
merge()
print(list_merge)
# 作业
list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2],
]
# 3. 定义向左移动函数,改变list_map中的数据
#    思路：将list_map每行赋值给list_merge
#         调用合并函数(练习2)

# 4. 定义向右移动函数,改变list_map中的数据
#    思路：将list_map每行,反转,赋值给list_merge
#         调用合并函数
#         因为切片反转会创建新容器,所以还需要将list_merge还原给list_map

# 温馨提示：画内存图哦
```

