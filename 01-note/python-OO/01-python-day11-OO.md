# Day 11   2021/1/14  星期四

---

# 封装

## 设计角度讲

- 分而治之 - 划分多个类
- 变则疏之 - 寻找变化点

```python
"""
    封装设计思想
        分而治之 - 划分多个类
        变则疏之 - 寻找变化点
"""

# 需求:老张开车去东北
# 步骤:
# 1. 识别对象(行为不同用类区分)
#    人      车
# 2. 分配职责
#    使用    行驶
# 3. 建立交互
#    老张的使用方法
#		 调用车的行驶方法

# 方法1:直接创建对象（将实例化对象写入需要调用的函数中）
# 语义:老张每次去东北,都使用新车.去东北玩的过程中，先造了一辆车，去完就把车销毁了
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self,position):
        print(self.name,"去",position)
        car = Car()
        car.run()  #存在栈帧中，调用完就销毁了

class Car:
    def run(self):
        print("行驶")


# 数据不同用对象区分
lz = Person("老张")
ll = Person("老李")
lz.use("东北")
"""

# 方法2:在构造函数中创建对象（将实例化对象作为属性，通过self.方式来调用）
# 语义:老张开自己的车去东北，关系绑死了，老张出生的时候，伴随着一辆汽车
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def use(self,position):
        print(self.name,"去",position)
        self.car.run()

class Car:
    def run(self):
        print("行驶")

lz = Person("老张")
lz.use("东北")
"""

# 方法3:定义类时不创建对象,通过参数传入
# 语义:老张使用交通工具去东北  老张去东北，没有车，别人给了他一辆车，车和老张没关系
class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self, vehicle, position):
        print(self.name, "去", position)
        vehicle.run()


class Car:
    def run(self):
        print("行驶")


lz = Person("老张")
car = Car()
lz.use(car, "东北")
```



## 快捷键

自动生成函数 option+回车





# homework

1.三合一
2.当天练习独立完成
3.需求：小明使用手机打电话
4.需求：
    玩家攻击敌人,敌人受伤(减少血量,掉落装备),如果死亡,则加分.
    敌人攻击玩家,玩家受伤(减少血量,闪现红屏),如果死亡,则游戏结束.
5.实现员工管理系统

```
class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid # 员工编号
        self.did = did # 部门编号
        self.name = name
        self.money = money
```

6. (选做)2048核心算法
   -- 定义向左移动函数,改变list_map中的数据
    思路：将list_map每行赋值给list_merge
         调用合并函数(练习2)

-- 定义向右移动函数,改变list_map中的数据
 思路：将list_map每行,反转,赋值给list_merge
      调用合并函数
      因为切片反转会创建新容器,所以还需要将list_merge还原给list_map