"""
    Python核心(1)
        二、容器
            种类与特点
                字符串str：存储字符编码,不可变,序列
                列表list：存储变量,可变,序列
                元组tuple：存储变量,不可变,序列
                字典dict：存储键值对,可变,散列
                         键不可变且唯一
                集合set：存储键,可变,散列
            可变：预留空间 + 自动扩容  [使用方便]
            不可变：按需分配   [性能高]
            序列：有顺序,连续空间,节省内存,[定位元素方便]
            散列：无顺序,分散过存储,占用内存多,[定位单个元素最快]
        三.函数
            设计理念：崇尚小而精,拒绝大而全.
            参数：
                实参：与形参对应方式
                    位置实参：按顺序
                        函数名(数据1,数据2)
                    关键字实参：按名字
                        函数名(形参名1=数据1,形参名2=数据2)
                    序列实参：拆
                        函数名(*序列)
                    字典实参：拆
                        函数名(**字典)
                形参：约束实参传递方式
                    默认形参：可选
                        def 函数名(形参名1=数据1,形参名2=数据2)
                    位置形参：必填
                        def 函数名(形参名1,形参名2)
                    命名关键字形参：必须是关键字实参
                        def 函数名(*args,形参名1)
                        def 函数名(*,形参名1)
                    星号元组形参：合
                        def 函数名(*args)
                    双星号字典形参：合
                        def 函数名(**kwargs)
            可变与不可变数据传参
                函数内修改可变对象,无需通过return返回结果



"""
list01 = [10,5,4,5,65,78]
list02 = [10,5,4,5,65,78]
list03 = list01
# 判断2个变量所存储的地址是否相同
print(list01 is list02) # False
print(list01 is list03) # True

new_list = sorted(list01,reverse=True)
print(new_list)

def func01(p1):
    # 修改栈帧变量
    # p1 = [10,20,30]
    # 修改可变对象
    p1[0] = 10
    # p1[:] = [10,20,30]

list04 = [1,2,3]
func01(list04)
print(list04) # ?