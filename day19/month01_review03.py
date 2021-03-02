"""
    面向对象
        流程：
            客观事物 -抽象-> 类 -具体-> 对象
        类和对象
            class 类名:
                # 不同对象相同数据
                类变量 = 数据

                @classmethod
                def 类方法(cls):
                    ...

                def __init__(self,参数):
                    # 不同对象不同数据
                    self.实例变量 = 参数

                def 实例方法(self):
                    ...

                @staticmethod
                def 静态方法():
                    ...

            对象名 = 类名(数据)
            对象名.实例成员
            类名.类成员
            类名.静态方法
        三大特征
            封装
                -- 数据角度
                class 类名:
                    def __init__(self,参数1,参数2,参数3):
                        self.变量1 = 参数1
                        self.变量2 = 参数2
                        self.变量3 = 参数3
                -- 行为角度
                class 类名：
                    def __init__(self,参数2):
                        self.__变量1 = 数据
                        self.变量名2 = 参数2

                    def __方法1(self):
                        ...

                    @property
                    def 变量名2(self):
                        return self.__变量名2

                    @变量名2.setter
                    def 变量名2(self, value):
                        self.__变量名2 = value

            继承
                class 爸爸:
                    def __init__(self,参数1):
                        self.数据1 = 参数1
                    def 方法名1(self):
                        ...

                class 儿子(爸爸):
                    def __init__(self,参数1,参数2):
                        super().__init__(参数1)
                        self.数据2 = 参数2

                    def 方法名2(self):
                        self.方法名1()
            多态
                def 客户端代码(爸爸):
                    # 1. 调用父
                    # 编码时 调用父类方法
                    # 运行时 执行子类方法
                    爸爸.方法名1()

                class 爸爸:
                    def 方法名1(self):
                        ...

                class 儿子(爸爸):
                     # 2. 子重写
                     def 方法名1(self):
                        super().方法名1()
                        ...

                # 3. 创建子
                客户端代码(儿子())

        MVC 软件架构
            -- model.py
            calss XXModel: # 封装数据
                def __init__(self,参数1,参数2,参数3):
                    self.变量1 = 参数1
                    self.变量2 = 参数2
                    self.变量3 = 参数3
            -- usl.py
            class XXView: # 界面逻辑
                def __init__(self):
                    self.__controller = XXController()

                def 方法1(self):
                    self.__controller.方法3()

                def 方法2(self):
                    model = XXModel(数据1,数据2,数据3)
                    self.__controller.方法4(model)
            -- bll.py
            class XXController: # 核心逻辑
                def 方法3(self):
                    ...

                def 方法4(self,model):
                    ...
            -- main.py
            view = XXView()
            view.main()
"""
