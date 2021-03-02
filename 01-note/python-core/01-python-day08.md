# Day 08   2021/1/11  星期一



# 函数

- 用于封装一个特定的功能，表示一个功能或者行为。
-  函数是可以重复执行的语句块, 可以重复调用。

## 作用

提高代码的可重用性和可维护性（代码层次结构更清晰）。

## 定义函数

- 语法：

  def 函数名(形式参数):函数名（动词，小写_小写 _小写)

    	 函数体

- 说明：

  def 关键字：全称是define，意为”定义”。

  函数名：对函数体中语句的描述，规则与变量名相同。

  形式参数：方法定义者要求调用者提供的信息。

  函数体：完成该功能的语句。

- 函数的第一行语句建议使用文档字符串描述函数的功能与参数。

## 调用函数

- 语法：函数名(实际参数) 

- 说明：根据形参传递内容。

```python
# 练习2：定义函数,根据总两数,计算几斤零几两.:
#  提示：使用容器包装需要返回的多个数据
# total_liang = int(input("请输入两:"))
# jin = total_liang // 16
# liang = total_liang % 16
# print(str(jin) + "斤零" + str(liang) + "两")


def calculate(total_liang):
    jin = total_liang // 16
    liang = total_liang % 16
    return jin,liang

total_liang = int(input("请输入两:"))

jin,liang = calculate(total_liang)
print(f"{jin}斤零{liang}两")
```

```python
"""
    练习3：创建函数,根据课程阶段计算课程名称.
    number = input("请输入课程阶段数：")
    if number == "1":
        print("Python语言核心编程")
    elif number == "2":
        print("Python高级软件技术")
    elif number == "3":
        print("Web全栈")
    elif number == "4":
        print("网络爬虫")
    elif number == "5":
        print("数据分析、人工智能")
"""


def get_course_name(number):
    """
        获取课程名称
    :param number:int类型,课程阶段编号
    :return:课程名称
    """
    tuple_coures = (
        "Python语言核心编程",
        "Python高级软件技术",
        "Web全栈",
        "网络爬虫",
        "数据分析、人工智能"
    )
    if 1 <= number <= len(tuple_coures):
        return tuple_coures[number - 1]


print(get_course_name(10))
```

```python
"""
    练习4：创建函数,计算梯形面积.
        top_base = float(input("请输入上底："))
        bottom_base = float(input("请输入下底："))
        height = float(input("请输入高："))
        result = (top_base + bottom_base) * height / 2
        print("梯形面积是：" + str(result))
"""
def calculate_trapezoid_area(top_base, bottom_base, height):
    """
        计算梯形面积
    :param top_base:上底
    :param bottom_base:下底
    :param height:高
    :return:面积
    """
    return (top_base + bottom_base) * height / 2

# 调用函数：
#   函数名称(具体数据)
print(calculate_trapezoid_area(2, 3, 4))

```

```python
"""
    练习7：创建函数,根据年月计算天数.
            如果2月是闰年,则29天
            　　　 平年    28
    month = int(input("请输入月份:"))
    if 1 <= month <= 12:
        if month == 2:
            print("29天")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("30天")
        else:# 1 3 5 7 8 10 12
            print("31天")
    else:
        print("月份有误")

    year = int(input("请输入年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
"""
# def get_day_by_month(month):
#     if 1 <= month <= 12:
#         if month == 2:
#             return 2
#         elif month == 4 or month == 6 or month == 9 or month == 11:
#             return 30
#         else:
#             return 31
#     else:
#         return None

def is_leap_year(year):
    """
        判断是否为闰年
    :param year: 年份
    :return: bool类型,True表达是闰年,False表达不是闰年(是平年)
    """
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_day_by_month(year,month):
    """
        根据月份获取天数
    :param year:年份
    :param month:月份
    :return:天数
    """
    if 1 <= month <= 12:
        if month == 2:
            return 29 if is_leap_year(year) else 28
        if month in (4, 6, 9, 11):
            return 30
        return 31

print(get_day_by_month(2021,2))
```

# 函数内存分布

pass填充语法空白

```python
"""
    函数内存分布
"""


# 1. 将函数代码加载到内存中,函数体不执行.
def func01():
    a = 10
    print("func01执行了")


# 2. 调用函数时,在内存中开辟空间(栈帧),
#    存储在函数内部创建的变量。
func01()


# 3. 函数执行后,栈帧立即释放.

def func02(p1, p2):
    # 修改栈帧中的变量
    p1 = 100
    # 修改传入的列表
    p2[0] = 200


data01 = 10
data02 = [20]
func02(data01, data02)
print(data01)  # 10
print(data02)  # 200
```

## 可变／不可变类型在传参时的区别

1. 不可变类型参数有:

   数值型(整数，浮点数)

   布尔值bool

   None 空值

   字符串str

   元组tuple

2. 可变类型参数有:

   列表 list

   字典 dict

   集合 set

3. 传参说明：

   - 不可变类型的数据传参时，函数内部不会改变原数据的值。

   - 可变类型的数据传参时，函数内部可以改变原数据。

    

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210111145807183.png" alt="image-20210111145807183" style="zoom:50%;" />

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210111145836531.png" alt="image-20210111145836531" style="zoom:50%;" />

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210111145902423.png" alt="image-20210111145902423" style="zoom:50%;" />





## 快捷键

Command + P        参数信息（在方法中调用参数）

Ctrl + J       快速查看文档

Ctrl + Alt + M  提取方法



shift+command+L 改名



# 变量作用域

```python
"""
    变量作用域
        定义：
            变量起作用的范围
        适用性：
            在小范围(1个函数)内需要操作的数据使用局部变量
            在大范围(2个以上函数)内需要操作的数据使用全局变量
"""
# 2. 全局作用域:文件内部
#   全局变量:在全部作用域内创建的变量
#   适用范围:整个文件
data02 = 20
data03 = [30]

def func01():
    # 1. 局部作用域:函数内部
    # 局部变量:在局部作用域内创建的变量
    # 适用范围:一个函数
    data01 = 10
    print(data01)
    print(data02)

def func02():
    # print(data01) # 不能访问其他函数局部变量
    print(data02) # 读取全局变量

def func03():
    # 在局部作用域中不能修改全局变量
    # data02 = 200
    # 必须通过global语句声明
    global data02
    data02 = 200

def func04():
    # 没有修改全局变量
    # 在修改全局变量指向的列表
    # 所以不需要通过global语句声明
    data03[0] = 300

func01()
func02()
func03()
func04()
print(data02) # 200
print(data03) # [300]
```

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210111184000770.png" alt="image-20210111184000770" style="zoom:50%;" />

# 参数

```python
"""
    函数参数
        实际参数
        形式参数
"""


def fun01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

# 位置形参:实参必填
# 默认形参:实参可选
# 注意2:默认形参必须从右向左依次存在
def func02(p1 =0, p2="", p3=100):
    print(p1)
    print(p2)
    print(p3)

# 1. 位置实参:根据顺序与形参进行对应
fun01(1, 2, 3)

# 2. 关键字实参:根据名字与形参进行对应
fun01(p1=1, p2=2, p3=3)
fun01(p2=2, p1=1, p3=3)

# fun01(p2=2, p1=1)
# TypeError: fun01() missing 1 required positional argument: 'p3'

# fun01(1, 2) # 缺少参数
# TypeError: fun01() takes 3 positional arguments but 4 were given
# fun01(1, 2, 3, 4) # 参数过多

func02(p2=2)
func02(p2=2,p3=3)
# 支持同时使用位置实参与关键字实参
func02(1,p3=3)
# 注意1:先位置实参,后关键字实参
# func02(p1 =1,2,3)
```

# homework

1. 三合一

2. 当天练习独立完成

3. 定义函数,对数字列表进行升序排列

4. 创建函数,根据年龄计算人生阶段
   
    ```python
    age = int(input("请输入年龄："))
    if age <= 6:
        print("童年")
    elif age <= 17:  # 程序能执行到本行,说明age一定大于6
        print("少年")
    elif age <= 40:
        print("青年")
    elif age <= 65:
        print("中年")
    else:
        print("老年")
    ```
    

```python
def get_life_level(age):
    if age <= 6:
        return "童年"
    if age <= 17:
        return "少年"
    if age <= 40:
        return "青年"
    if age <= 65:
        return "中年"
    return "老年"

print(get_life_level(30))
```

5.

  ```python
  list_commodity_infos = [
   {"cid": 1001, "name": "屠龙刀", "price": 10000},
   {"cid": 1002, "name": "倚天剑", "price": 10000},
   {"cid": 1003, "name": "金箍棒", "price": 52100},
   {"cid": 1004, "name": "口罩", "price": 20},
   {"cid": 1005, "name": "酒精", "price": 30},
  ]
  list_orders = [
   {"cid": 1001, "count": 1},
   {"cid": 1002, "count": 3},
   {"cid": 1005, "count": 2},
  ]
  ```

  - 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.

  - 定义函数,打印商品单价小于2万的商品信息

  - (选做)定义函数,打印所有订单中的商品信息,
    格式：商品名称xx,商品单价:xx,数量xx.
    
  - 定义函数,查找单价最高的商品

  - 定义函数,根据单价升序排列

    ```python
    # --------------------------数据--------------------------
    # 商品列表
    # dict_commodity_infos = {
    #     1001:{"name": "屠龙刀", "price": 10000},
    #     1002:{"name": "倚天剑", "price": 10000},
    #     1003:{"name": "金箍棒", "price": 52100},
    #     1004:{"name": "口罩", "price": 20},
    #     1005:{"name": "酒精", "price": 30},
    # }
    list_commodity_infos = [
        {"cid": 1001, "name": "屠龙刀", "price": 10000},
        {"cid": 1002, "name": "倚天剑", "price": 10000},
        {"cid": 1003, "name": "金箍棒", "price": 52100},
        {"cid": 1004, "name": "口罩", "price": 20},
        {"cid": 1005, "name": "酒精", "price": 30},
    ]
    # 订单列表
    list_orders = [
        {"cid": 1001, "count": 1},
        {"cid": 1002, "count": 3},
        {"cid": 1005, "count": 2},
    ]
    
    #有相同的东西提出来成为函数
    def print_single_commodity(commodity):
        print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")
    
    # 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
    def print_commodity_infos():
        for commodity in list_commodity_infos:
            # print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")
            print_single_commodity(commodity)
    
    # 2.  定义函数,打印商品单价小于2万的商品信息
    def print_price_in_2w():
        for commodity in list_commodity_infos:
            if commodity["price"] < 20000:
                # print(f"编号:{commodity['cid']}商品名称:{commodity['name']}商品单价:{commodity['price']}")
                print_single_commodity(commodity)
    
    
    # 3.  定义函数,打印所有订单中的商品信息,
    #   格式：商品名称xx,商品单价:xx,数量xx.
    def print_order_infos():
        for order in list_orders:  # 遍历所有订单
            # order["cid"] --> 1001  -->
            for commodity in list_commodity_infos:  # 遍历所有商品信息
                # commodity["cid"] --> 1001
                # 使用订单中的商品编号 在 商品信息中查找(商品)
                if order["cid"] == commodity["cid"]:
                    print(f"商品名称{commodity['name']},商品单价:{commodity['price']},数量{order['count']}.")
                    break  # 跳出内层循环  找到之后后面的不用再比了
    
    
    # 4. 查找单价最高的商品
    def get_max_by_price():
        max_value = list_commodity_infos[0]
        for i in range(1, len(list_commodity_infos)):
            if max_value["price"] > list_commodity_infos[i]["price"]:
                max_value = list_commodity_infos[i]
        return max_value
    
    
    # 5. 根据单价升序排列
    def ascending_order_by_price():
        for r in range(len(list_commodity_infos) - 1):
            for c in range(r + 1, len(list_commodity_infos)):
                if list_commodity_infos[r]["price"] < list_commodity_infos[c]["price"]:
                    list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
    
    
    print_commodity_infos()
    print_price_in_2w()
    print_order_infos()
    print(get_max_by_price())
    ascending_order_by_price()
    print(list_commodity_infos)
    ```

    

6. (选做)定义函数,将列表中奇数删除
    测试数据:[3,7,5,6,7,8,9,13]
    提示:在列表中删除多个元素,倒序删除
    
    ```python
    list01 = [3, 7, 5, 6, 7, 8, 9, 13]
    
    # 问题1：漏删 -- 后面的元素向前挤.
    # 问题2：越界 -- 删除元素列表长度减少
    # for i in range(len(list01)):#0~7
    #     if list01[i] % 2:
    #         del list01[i]
    
    # 根据条件在容器中删除多个元素
    # 倒序删除
    def delete_all_by_odd(list_target):
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] % 2:
                del list_target[i]
    
    
    list01 = [3, 4, 5, 6, 7, 8, 9]
    delete_all_by_odd(list01)
    print(list01)
    ```
    
    