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

   