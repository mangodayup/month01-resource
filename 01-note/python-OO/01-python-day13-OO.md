# Day 13   2021/1/18  星期一

---

# 2048

## 怎么吹牛？

和技术谈深度，和人事谈广度

广度：一个技术的多个案例

深度：

- 谈架构：
              显示(界面)与控制(算法)分离
                  - 控制台
                                  - PyQt
                                  - PyGame

- 谈算法

      1. 高内聚:
              上下移动 -矩阵转置-> 左右移动
              向左移动 --> 合并数据 --> 零元素后移
              向右移动 -翻转-> 合并数据 --> 零元素后移
      2. 降维思想:（如何简化问题 ）
            将二维列表的操作,改为对一维列表的操作.

  ```python
  """
      2048 游戏核心算法
          谈架构
              显示(界面)与控制(算法)分离
                  控制台
                  PyQt
                  PyGame
  
          谈算法
              1. 高内聚:
                  上下移动 -矩阵转置-> 左右移动
                  向左移动 --> 合并数据 --> 零元素后移
                  向右移动 -翻转-> 合并数据 --> 零元素后移
              2. 降维思想:
                  将二维列表的操作,改为对一维列表的操作.
  """
  list_merge = [2, 0, 0, 2]
  
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
  
  # zero_to_end()
  # print(list_merge)
  
  
  # 2. 定义函数　merge()
  # [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
  # [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
  # [4,4,4,4]  -->  [8,8,0,0]
  # [2,0,4,2]  -->  [2,4,2,0]
  def merge():
      """
          合并数据
            核心思想：零元素后移，判断是否相邻相同。如果是则合并.
      """
      zero_to_end()
      for i in range(len(list_merge) - 1):
          if list_merge[i] == list_merge[i + 1]:
              list_merge[i] += list_merge[i + 1]
              del list_merge[i + 1]
              list_merge.append(0)
              # 加分
  
  # merge()
  # print(list_merge)
  
  # 3. 向左移动
  map = [
      [2, 0, 0, 2],
      [4, 2, 0, 2],
      [2, 4, 2, 4],
      [0, 4, 0, 4],
  ]
  
  def move_left():
      """
          向左移动map
          思想：获取每行，交给list_merge，在通知merge()进行合并
      :return:
      """
      global list_merge
      for line in map:
          list_merge = line
          merge()
  
  # move_left()
  # print(map)
  
  # 4. 向右移动 move_right
  def move_right():
      """
          向左移动map
          思想：获取每行，交给list_merge，在通知merge()进行合并
      :return:
      """
      global list_merge
      for line in map:
          # 从右向左获取数据形成新列表
          list_merge = line[::-1]
          # 处理数据
          merge()
          # 将处理后的数据再从右向左还给map
          line[::-1] = list_merge
  
  # move_right()
  # print(map)
  
  # 5. 向上移动 move_up   转置  move_left　转置
  def square_matrix_transposition():
      """
          方阵转置（列转换为行）
      :param map: 需要转置的方阵
      :return:
      """
      for c in range(1, len(map)):  # 1 2 3
          for r in range(c, len(map)):
              map[r][c - 1], map[c - 1][r] = map[c - 1][r], map[r][c - 1]
  
  def move_up():
      """
          向上移动
          思想：  转置  move_left　转置　
      """
      square_matrix_transposition()
      move_left()
      square_matrix_transposition()
  
  # 6. 向下移动
  def move_down():
      """
          向下移动
          思想: 转置  move_right　转置
      :return:
      """
      square_matrix_transposition()
      move_right()
      square_matrix_transposition()
  
  
  # move_up()
  move_down()
  print(map)
  ```

# 人使用手机的设计思想

封装[分]：根据行为的不同，划分类，遇到变化点，封装变化（识别变化）——创建人类和手机类

继承[隔]：当使用变化点的时候，让不同类型在一个行为上达到统一，（统一变化）——使用通信工具类，隔离人类与手机、座机等

多态[做]：框架先确定用法，实现类再完成做法

通过重写实现手机的功能

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210118152217399.png" alt="image-20210118152217399" style="zoom:50%;" />

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210118152301398.png" alt="image-20210118152301398" style="zoom:50%;" />

# 设计原则

## 开闭原则（目标、总的指导思想） 

**O**pen **C**losed **P**rinciple

对扩展开放，对修改关闭。

增加新功能，不改变原有代码。

## 类的单一原则（一个类的定义）

**S**ingle **R**esponsibility **P**rinciple  

一个类有且只有一个改变它的原因。

## 依赖倒置（依赖抽象）

引出了继承

**D**ependency **I**nversion **P**rinciple

客户端代码(调用的类)尽量依赖(使用)抽象。

抽象不应该依赖细节，细节应该依赖抽象。

## 组合复用（复用的最佳实践）

Composite Reuse Principle

如果仅仅为了代码复用优先选择组合复用，而非继承复用。

组合的耦合性相对继承低。

**继承的语义：是一种的关系 **is-a

**组合的语义：是有一个的关系（用变量的方式去调用）**has-a 例如：员工管理器和员工之间的关系是组合关系，连接员工薪资算法



继承关系统一变化  （父类在隔离某一个维度的变化）

组合关系连接变化

## 里式替换（继承后的重写，指导继承的设计）

**L**iskov **S**ubstitution **P**rinciple

父类出现的地方可以被子类替换，在替换后依然保持原功能。

子类要拥有父类的所有功能。

子类在重写父类方法时，尽量选择**扩展重写**，防止改变了功能。

扩展重写：建议先用super()调用父类方法，再增加新功能

## 迪米特法则（类与类交互的原则）

**L**aw **o**f **D**emeter

不要和陌生人说话。

类与类交互时，在满足功能要求的基础上，传递的数据量越少越好。因为这样可能降低耦合度。



```python
"""
    开闭原则：增加新岗位,员工管理器不变.
    单一职责:
        员工管理器负责统一管理所有员工,获取总薪资.
        程序员类负责程序员的薪资算法
        测试员类负责测试员的薪资算法
    依赖倒置:员工管理器调用员工类,不调用程序员/测试员.
    组合复用:
        员工管理器使用组合关系连接员工薪资算法
        没有通过继承调用员工薪资算法.
    里氏替换:
        员工管理器添加员工方法,形参是员工,实参是程序员/测试员
        程序员/测试员在重写时,先通过super()调用员工方法,再定义新算法.
        扩展重写:先通过super()调用父类方法
                再增加新功能
    迪米特法则:
        员工管理器与程序员/测试员是低耦合关系
"""

from typing import List


# ---------架构师----------

class Employee:
    def __init__(self, base_salary=0):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary * 0.8


class EmployeeController:
    def __init__(self):
        self.__all_employee = []  # type:List[Employee]

    def add_emp(self, emp: Employee):
        self.__all_employee.append(emp)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__all_employee:
            # 先确定用法
            # 1. 编码时 调用父
            #    运行时 执行子
            total_salary += item.calculate_salary()
        return total_salary


# ---------程序员----------

class Programmer(Employee):
    def __init__(self, base_salay=0, bonus=0):
        super().__init__(base_salay)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

    # 后确定做法(符合/遵守 用法)
    # 2. 子重写


class Tester(Employee):
    def __init__(self, base_salary=0, bug_count=0):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5


# 入口
controller = EmployeeController()
# 3. 创建子
controller.add_emp(Programmer(10000, 1000000))
controller.add_emp(Tester(8000, 2000))
print(controller.get_total_salary())
```

# 多继承

**super找的是继承列表里的第一个**

一个子类继承两个或两个以上的基类，父类中的属性和方法同时被子类继承下来。

同名方法的解析顺序（MRO， Method Resolution Order）:

类自身 --> 父类继承列表（由左至右）--> 再上层父类

​    A                   

   / \

   /  \

  B   C         

   \  /

   \ /

​    D        

```python
class A:
    def func01(self):
        print("A")
        super().func01()


class B:
    def func01(self):
        print("B")


class C(A,B):
    def func01(self):
        print("C")
        super().func01()


class D(A, B):
    def func01(self):
        print("D")
        super().func01()

#如果指定某个父类的同命方法，需要使用类名.实例方法名(self)
#eg: B.func01(self)

class E(C,D):
    def func01(self):
        print("E")
        super().func01()

e = E()
e.func01()

#输出结果
#E
#C
#D
#A
#B


#D.mro()打印出继承关系

```

```python
教师1 = 教师_A校区(…)
学生1 = 学生_实验室和宿舍同地(…)
审核出入校(教师1)
审核出入校(学生1)
```

