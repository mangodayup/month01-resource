"""
    商品管理系统
"""


class CommodityModel:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    """
        商品视图
    """

    def __init__(self):
        self.__controller = CommodityController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = int(input("请输入商品单价:"))
        self.__controller.add_commodity(commodity)

    def __display_commoditys(self):
        for item in self.__controller.list_commoditys:
            print(f"{item.name}的编号是{item.cid},单价是{item.price}")

    def __delete_commodity(self):
        cid = int(input("请输入商品编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        cmd = CommodityModel()
        cmd.cid = int(input("请输入商品编号:"))
        cmd.name = int(input("请输入商品名称:"))
        cmd.price = int(input("请输入商品单价:"))
        if self.__controller.update_commodity(cmd):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    """
        控制器
    """

    __start_id = 1001

    @classmethod
    def __set_cid(cls, cmd):
        cmd.cid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__list_commoditys = []

    @property
    def list_commoditys(self):
        return self.__list_commoditys

    def add_commodity(self, cmd):
        CommodityController.__set_cid(cmd)
        self.__list_commoditys.append(cmd)

    def remove_commodity(self, cid):
        """
            移除商品信息
        :param cid: 商品编号
        :return: 是否移除成功
        """
        for i in range(len(self.__list_commoditys)):
            if self.__list_commoditys[i].cid == cid:
                del self.__list_commoditys[i]
                return True
        return False

    def update_commodity(self, cmd):
        """
            更新商品信息
        :param cmd: 需要更新的商品信息
        :return: 更新是否成功
        """
        for item in self.__list_commoditys:
            if item.cid == cmd.cid:
                item.__dict__ = cmd.__dict__
                return True
        return False


view = CommodityView()
view.main()
